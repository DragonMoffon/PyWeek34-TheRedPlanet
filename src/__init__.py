from arcade.resources import add_resource_handle

from src.engine import _Engine
from src.input import Input

from src.constants import update_rate, draw_rate, screen_width, screen_height

Engine: _Engine = None


def launch():
    global Engine

    add_resource_handle("data", "resources")

    Engine = _Engine(screen_width, screen_height, update_rate, draw_rate)
    Input.setup_keys()
    Engine.run()
