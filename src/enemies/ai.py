from src.input import InputStream


class Ai:

    def __init__(self, input_target: InputStream = None):
        self._input_target = input_target or InputStream()
        self._input_target.setup_keys()

    @property
    def Input(self):
        return self._input_target
