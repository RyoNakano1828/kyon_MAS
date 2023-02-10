import mesa
from kyon.random_walk import RandomWalker


class Sheep(RandomWalker):
    """
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the RandomWalker.
    """

    energy = None
    after_birth = 0

    def __init__(self, unique_id, pos, model, moore, energy=None, sheep_reproduce_count=False, after_birth=0, is_eat=False):
        super().__init__(unique_id, pos, model, moore=moore)
        self.energy = energy
        self.sheep_reproduce_count=False
        self.after_birth=after_birth
        self.is_eat=False

    def step(self):
        """
        A model step. Move, then eat grass and reproduce.
        """
        self.random_move()
        living = True
        self.sheep_reproduce_count = False
        self.after_birth += 1
        self.is_eat=False

        if self.model.grass:
            # Reduce energy
            self.energy -= 1

            # If there is grass available, eat it
            this_cell = self.model.grid.get_cell_list_contents([self.pos])
            grass_patch = [obj for obj in this_cell if isinstance(obj, GrassPatch)][0]
            if grass_patch.fully_grown:
                self.energy += self.model.sheep_gain_from_food
                grass_patch.fully_grown = False
                self.is_eat=True

            # # Death
            # if self.energy < 0:
            #     self.model.grid.remove_agent(self)
            #     self.model.schedule.remove(self)
            #     living = False

        # Death（年齢が高くなるほど死亡率があがる）
        if self.random.random() < (self.model.sheep_reproduce/5)*(self.after_birth/540):
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            living = False

        # Born
        if living and self.after_birth >= 150 and self.random.random() < self.model.sheep_reproduce/2:
            # Create a new sheep:
            if self.model.grass:
                self.energy /= 2
            lamb = Sheep(
                self.model.next_id(), self.pos, self.model, self.moore, self.energy, self.sheep_reproduce_count, 0
            )
            self.model.grid.place_agent(lamb, self.pos)
            self.model.schedule.add(lamb)
            self.sheep_reproduce_count = True


class Wolf(RandomWalker):
    """
    A wolf that walks around, reproduces (asexually) and eats sheep.
    """

    energy = None

    def __init__(self, unique_id, pos, model, moore, energy=None, is_hunt=False):
        super().__init__(unique_id, pos, model, moore=moore)
        self.energy = energy
        self.is_hunt = False

    def step(self):
        self.random_move()
        self.energy -= 1
        self.is_hunt = False

        # If there are sheep present, eat one
        x, y = self.pos
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        sheep = [obj for obj in this_cell if isinstance(obj, Sheep)]
        if len(sheep) > 0:
            sheep_to_eat = self.random.choice(sheep)
            self.energy += self.model.wolf_gain_from_food

            # Kill the Kyon
            if self.random.random() < self.model.capture_success_rate:
                self.model.grid.remove_agent(sheep_to_eat)
                self.model.schedule.remove(sheep_to_eat)
                self.is_hunt = True

        # Death or reproduction
        # if self.energy < 0:
        #     self.model.grid.remove_agent(self)
        #     self.model.schedule.remove(self)
        # else:
        #     if self.random.random() < self.model.wolf_reproduce:
        #         # Create a new wolf cub
        #         self.energy /= 2
        #         cub = Wolf(
        #             self.model.next_id(), self.pos, self.model, self.moore, self.energy
        #         )
        #         self.model.grid.place_agent(cub, cub.pos)
        #         self.model.schedule.add(cub)


class GrassPatch(mesa.Agent):
    """
    A patch of grass that grows at a fixed rate and it is eaten by sheep
    """

    def __init__(self, unique_id, pos, model, fully_grown, countdown):
        """
        Creates a new patch of grass

        Args:
            grown: (boolean) Whether the patch of grass is fully grown or not
            countdown: Time for the patch of grass to be fully grown again
        """
        super().__init__(unique_id, model)
        self.fully_grown = fully_grown
        self.countdown = countdown
        self.pos = pos

    def step(self):
        if not self.fully_grown:
            if self.countdown <= 0:
                # Set as fully grown
                self.fully_grown = True
                self.countdown = self.model.grass_regrowth_time
            else:
                self.countdown -= 1
