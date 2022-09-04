from arcade import Window
import arcade.key as keys

from src.clock import Clock
from src.input import Input

from time import time


class _Engine(Window):

    def __init__(self, width, height, draw_rate, update_rate):
        super().__init__(width, height, "Dragon's Bakery - PyWeek 34 - The Red Planet",
                         update_rate=update_rate, draw_rate=draw_rate, fullscreen=True)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == keys.ESCAPE:
            self.close()
        else:
            Input.key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        Input.key_release(symbol, modifiers)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print("clicky")
        Input.key_press(button, modifiers)
        Input.update_mouse(x, y)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        print("clacky")
        Input.key_release(button, modifiers)
        Input.update_mouse(x, y)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        print("movey")
        Input.update_mouse(x, y, dx, dy)

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        print("draggy")
        Input.update_mouse(x, y, dx, dy)

    def on_update(self, delta_time: float):
        Clock.tick(delta_time)

    def on_draw(self):
        self.clear()
