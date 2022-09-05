from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.engine import _Engine

from arcade import View, Camera
from arcade.background import Background

from src.input import Input
from src.clock import Clock

from time import time


class MissionView(View):

    def __init__(self, engine: '_Engine'):
        super().__init__(engine)
        self._engine: '_Engine' = engine
        self._camera = Camera(engine.width, engine.height, engine)

        self._background = Background.from_file(":data:/textures/tile_1.png",
                                                size=(self.window.width, self.window.height))

    def on_update(self, delta_time):
        Clock.tick(delta_time)

        self._engine.player.mission_update()

    def on_draw(self):
        self._camera.use()
        self.clear()
        self._background.draw()
        self._engine.player.draw()

    def on_show_view(self):
        pass
        # self._camera.zoom(2.0)
