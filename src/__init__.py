from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.clock import _Clock

from arcade.resources import add_resource_handle

from src.engine import _Engine
from src.input import process_key_data
from src.constants import update_rate, draw_rate, screen_width, screen_height

Engine: _Engine = None


def launch():
    global Engine

    add_resource_handle("data", "resources")

    Engine = _Engine(screen_width, screen_height, update_rate, draw_rate)
    process_key_data()
    Engine.run()
