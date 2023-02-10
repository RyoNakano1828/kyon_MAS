import mesa

from kyon.agents import Wolf, Sheep, GrassPatch
from kyon.model import WolfSheep


def wolf_sheep_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Sheep:
        portrayal["Shape"] = "kyon/resources/kyon.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1
        portrayal["text"] = round(agent.after_birth, 1)
        portrayal["text_color"] = "Black"


    elif type(agent) is Wolf:
        portrayal["Shape"] = "kyon/resources/hunter.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 2
        portrayal["text"] = round(agent.energy, 1)
        portrayal["text_color"] = "White"

    elif type(agent) is GrassPatch:
        if agent.fully_grown:
            portrayal["Color"] = ["#00FF00", "#00CC00", "#009900"]
        else:
            portrayal["Color"] = ["#84e184", "#adebad", "#d6f5d6"]
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1

    return portrayal


canvas_element = mesa.visualization.CanvasGrid(wolf_sheep_portrayal, 40, 40, 1000, 1000)
chart_element = mesa.visualization.ChartModule(
    [
        # {"Label": "Wolves", "Color": "#AA0000"},
        {"Label": "Kyon", "Color": "#666666"},
        # {"Label": "EatenGrass", "Color": "#00AA00"},
    ]
)

chart_element2 = mesa.visualization.ChartModule(
    [
        {"Label": "BornKyon", "Color": "#00AA00"},
        {"Label": "DeadinLifeKyon", "Color": "#666666"},
        {"Label": "HuntedKyon", "Color": "#AA0000"},
    ]
)

chart_element3 = mesa.visualization.ChartModule(
    [
        {"Label": "EatenGrass", "Color": "#00AA00"},
    ]
)

model_params = {
    # The following line is an example to showcase StaticText.
    "title": mesa.visualization.StaticText("Parameters:"),
    # "grass": mesa.visualization.Checkbox("Grass Enabled", True),
    "grass_regrowth_time": mesa.visualization.Slider("Grass Regrowth Time", 1, 1, 10),
    "initial_sheep": mesa.visualization.Slider(
        "Initial Kyon Population", 250, 10, 300
    ),
    "sheep_reproduce": mesa.visualization.Slider(
        "Kyon Reproduction Rate", 0.005, 0.001, 1.0, 0.001
    ),
    "initial_wolves": mesa.visualization.Slider("Initial Hunter Population", 10, 0, 100),
    "capture_success_rate": mesa.visualization.Slider(
        "Kyon Capture Success Rate", 0.1, 0.01, 1.0, 0.01
    ),
    "simuration_counter": mesa.visualization.Slider("Simuration Counter", 1, 1, 10),
    # "wolf_reproduce": mesa.visualization.Slider(
    #     "Hunter Reproduction Rate",
    #     0.0,
    #     0.0,
    #     1.0,
    #     0.01,
    #     description="The rate at which hunter agents reproduce.",
    # ),
    # "wolf_gain_from_food": mesa.visualization.Slider(
    #     "Hunter Gain From Food Rate", 0, 0, 50
    # ),
    # "sheep_gain_from_food": mesa.visualization.Slider("Kyon Gain From Food", 4, 1, 10),
}

server = mesa.visualization.ModularServer(
    WolfSheep, [], "Kyon Breeding Simulation", model_params
    # WolfSheep, [canvas_element, chart_element, chart_element2, chart_element3], "Kyon Breeding Simulation", model_params
)
server.port = 8522
