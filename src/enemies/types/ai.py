from src.input import InputStream

from src.enemies.types.data import Data


class Ai:

    def __init__(self, data: Data, input_target: InputStream = None):
        self._data = data

        self._input_target = input_target or InputStream()
        self._input_target.setup_keys()

        self._target_position = self._data.position
        self._target_aim = (0, 0)

    @property
    def Input(self):
        return self._input_target

    @property
    def target_pos(self):
        return self._target_position

    @property
    def target_aim(self):
        return self._target_aim

    def step(self):
        pass
