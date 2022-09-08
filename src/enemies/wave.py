from src.enemies.types import ENEMIES


class Wave:

    def __init__(self, data, door):
        self._enemy_data = data

        self._door = door

        self._enemies = []
        for enemy in data:
            _type = ENEMIES[enemy]
            self._enemies.append(_type())  #TODO: Add enemy specific data.

    @property
    def enemies(self):
        return self._enemies
