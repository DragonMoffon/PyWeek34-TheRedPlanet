from arcade.resources import add_resource_handle
from src.engine import _Engine

Engine: _Engine = None
Clock: "_Clock" = None


def launch():
    global Engine
    global Clock

    engine_rate = 1/120  # The update speed of the game. at 1/120 the engine will try run at 120 fps.

    add_resource_handle("data", "resources")

    Engine = _Engine(800, 600, engine_rate, engine_rate)
    Clock = Engine.clock

    Engine.run()
