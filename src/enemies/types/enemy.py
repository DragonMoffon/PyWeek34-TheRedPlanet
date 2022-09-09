from src.enemies.types.data import Data
from src.enemies.types.ai import Ai


class Enemy:
    # TODO: Add a way to tell manager and wave that the enemy was killed.

    def __init__(self, ai: Ai, data: Data):
        self._ai = ai
        self._data = data

    @property
    def sprite(self):
        return self._data.sprite

    @property
    def health(self):
        return self._data.health

    def damage(self, damage=1):
        self._data.health -= 1
        print(self._data.health)

    def place(self, x, y):
        _x = 1000 + x*32
        _y = 500 + y*32
        self._data.position = (_x, _y)

    def ai_step(self):
        self._ai.step()

    def update(self):
        pass
