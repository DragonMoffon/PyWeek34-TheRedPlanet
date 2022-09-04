from arcade import Window
from src.clock import _Clock
from src.inputs import _InputStream


class _Engine(Window):

    def __init__(self, width, height, draw_rate, update_rate):
        super().__init__(width, height, "Dragon's Bakery - PyWeek 34 - The Red Planet",
                         update_rate=update_rate, draw_rate=draw_rate, fullscreen=True)
        self.clock = _Clock(1, update_rate)
        self.inputs = _InputStream()

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_update(self, delta_time: float):
        self.clock.tick(delta_time)

    def on_draw(self):
        self.clear()
