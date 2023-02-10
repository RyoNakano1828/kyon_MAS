"""
Wolf-Sheep Predation Model
================================

Replication of the model found in NetLogo:
    Wilensky, U. (1997). NetLogo Wolf Sheep Predation model.
    http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation.
    Center for Connected Learning and Computer-Based Modeling,
    Northwestern University, Evanston, IL.
"""

import mesa
import numpy as np
from scipy.stats import lognorm
import numpy as np

from kyon.scheduler import RandomActivationByTypeFiltered
from kyon.agents import Sheep, Wolf, GrassPatch
import pandas as pd

class WolfSheep(mesa.Model):
    """
    Wolf-Sheep Predation Model
    """

    height = 40
    width = 40

    initial_sheep = 250
    initial_wolves = 50

    sheep_reproduce = 0.005
    wolf_reproduce = 0

    capture_success_rate=0.1

    wolf_gain_from_food = 0

    grass = True
    grass_regrowth_time = 3
    sheep_gain_from_food = 4
    simuration_counter = 1

    verbose = False  # Print-monitoring

    description = (
        "Kyon breeding simulation Model"
    )

    
    

    def __init__(
        self,
        width=40,
        height=40,
        initial_sheep=250,
        initial_wolves=50,
        sheep_reproduce=0.005,
        wolf_reproduce=0,
        wolf_gain_from_food=0,
        grass=True,
        grass_regrowth_time=3,
        sheep_gain_from_food=4,
        capture_success_rate=0.1,
        simuration_counter=1,
    ):
        """
        Create a new Wolf-Sheep model with the given parameters.

        Args:
            initial_sheep: Number of sheep to start with
            initial_wolves: Number of wolves to start with
            sheep_reproduce: Probability of each sheep reproducing each step
            wolf_reproduce: Probability of each wolf reproducing each step
            wolf_gain_from_food: Energy a wolf gains from eating a sheep
            grass: Whether to have the sheep eat grass for energy
            grass_regrowth_time: How long it takes for a grass patch to regrow
                                 once it is eaten
            sheep_gain_from_food: Energy sheep gain from grass, if enabled.
        """
        super().__init__()
        # Set parameters
        self.width = width
        self.height = height
        self.initial_sheep = initial_sheep
        self.initial_wolves = initial_wolves
        self.sheep_reproduce = sheep_reproduce
        self.wolf_reproduce = wolf_reproduce
        self.wolf_gain_from_food = wolf_gain_from_food
        self.grass = grass
        self.grass_regrowth_time = grass_regrowth_time
        self.sheep_gain_from_food = sheep_gain_from_food
        self.capture_success_rate = capture_success_rate
        self.simuration_counter = simuration_counter

        self.schedule = RandomActivationByTypeFiltered(self)
        self.grid = mesa.space.MultiGrid(self.width, self.height, torus=True)
        self.increased_Kyon = 0
        self.kyon_nums = []
        self.eaten_kyons = []
        self.dead_kyons = []
        self.born_kyons = []
        self.eaten_grasses = []
        self.kyon_increase = []
        self.datacollector = mesa.DataCollector(
            {
                "Wolves": lambda m: m.schedule.get_type_count(Wolf),
                "Kyon": lambda m: m.schedule.get_type_count(Sheep),
                "Grass": lambda m: m.schedule.get_type_count(
                    GrassPatch, lambda x: x.fully_grown
                ),
                "EatenGrass": lambda m: m.schedule.get_type_count(
                    Sheep, lambda x: x.is_eat
                ),
                "BornKyon":lambda m: m.schedule.get_type_count(
                    Sheep, lambda x: x.sheep_reproduce_count
                ),
                "DeadinLifeKyon":lambda m:m.schedule.get_type_count(Sheep, lambda x: x.sheep_reproduce_count) - m.schedule.get_type_count(Wolf, lambda x: x.is_hunt) - m.increased_Kyon,
                "HuntedKyon":lambda m: m.schedule.get_type_count(
                    Wolf, lambda x: x.is_hunt
                ),
                "IncreasedKyon":lambda m:m.increased_Kyon,
            }
        )

        data = lognorm(s=0.5, scale=540).rvs(size=self.initial_sheep)
        age_distribution = []
        for d in data:
            age_distribution.append(round(d))

        # Create sheep:
        for i in range(self.initial_sheep):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            energy = self.random.randrange(2 * self.sheep_gain_from_food)
            # print(type(energy))
            sheep = Sheep(self.next_id(), (x, y), self, True, energy, False, int(age_distribution[i]))
            self.grid.place_agent(sheep, (x, y))
            self.schedule.add(sheep)

        # Create wolves
        for i in range(self.initial_wolves):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            # energy = self.random.randrange(2 * self.wolf_gain_from_food)
            energy = self.random.randrange(2)
            wolf = Wolf(self.next_id(), (x, y), self, True, energy)
            self.grid.place_agent(wolf, (x, y))
            self.schedule.add(wolf)

        # Create grass patches
        if self.grass:
            for agent, x, y in self.grid.coord_iter():

                fully_grown = self.random.choice([True, False])

                if fully_grown:
                    countdown = self.grass_regrowth_time
                else:
                    countdown = self.random.randrange(self.grass_regrowth_time)

                patch = GrassPatch(self.next_id(), (x, y), self, fully_grown, countdown)
                self.grid.place_agent(patch, (x, y))
                self.schedule.add(patch)

        self.running = True
        self.counter = 0
        self.before_kyon_count = self.initial_sheep
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
 
        self.increased_Kyon = self.schedule.get_type_count(Sheep) - self.before_kyon_count
        # collect data
        self.datacollector.collect(self)

        self.before_kyon_count = self.schedule.get_type_count(Sheep)

        '''
        # キョンの増減数 = 子を産んだキョン - 捉えられたキョン - 寿命で死んだキョン
        # 寿命で死んだキョン = 子を産んだキョン - 捉えられたキョン - キョンの増減数

        # キョンの数
        print(f"キョンの数：{self.schedule.get_type_count(Sheep)}")
        
        # 子を産んだキョンの数
        print(f"子を産んだキョン：{self.schedule.get_type_count(Sheep, lambda x: x.sheep_reproduce_count)}")

        # 捉えられたキョンの数
        print(f"捉えられたキョン：{self.schedule.get_type_count(Wolf, lambda x: x.is_hunt)}")

        # 寿命で死んだキョン
        print(f"寿命で死んだキョン：{self.schedule.get_type_count(Sheep, lambda x: x.sheep_reproduce_count) - self.schedule.get_type_count(Wolf, lambda x: x.is_hunt) - self.increased_Kyon}")

        # キョンの増減数
        print(f"キョンの増減数：{self.increased_Kyon}")

        # キョンが食べた草の数
        print(f"キョンが食べた草の数：{self.schedule.get_type_count(Sheep, lambda x: x.is_eat)}")

        '''

        self.kyon_nums.append(self.schedule.get_type_count(Sheep))
        self.eaten_kyons.append(self.schedule.get_type_count(Wolf, lambda x: x.is_hunt))
        self.dead_kyons.append(self.schedule.get_type_count(Sheep, lambda x: x.sheep_reproduce_count) - self.schedule.get_type_count(Wolf, lambda x: x.is_hunt) - self.increased_Kyon)
        self.born_kyons.append(self.schedule.get_type_count(Sheep, lambda x: x.sheep_reproduce_count))
        self.eaten_grasses.append(self.schedule.get_type_count(Sheep, lambda x: x.is_eat))
        self.kyon_increase.append(self.increased_Kyon)

        self.counter += 1

        if self.counter == 365*6:
            df_result = pd.DataFrame({
                "kyon_nums": self.kyon_nums,
                "eaten_kyons": self.eaten_kyons,
                "dead_kyons": self.dead_kyons,
                "born_kyons": self.born_kyons,
                "eaten_grasses": self.eaten_grasses,
                "increase": self.kyon_increase
            })

            print(df_result)

            df_result.to_csv(f"{self.initial_sheep}_{self.initial_wolves}_{self.capture_success_rate}_result_{self.simuration_counter}.csv")

            self.running = False
