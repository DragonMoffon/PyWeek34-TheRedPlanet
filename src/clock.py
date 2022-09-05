from src.constants import clock_speed, update_rate


class _Clock:

    def __init__(self, speed, frame_speed):
        self._speed = speed  # the time multiplier (game runs at half speed when speed = 0.5)
        self._frame_speed = frame_speed  # equal to the update rate

        self._current_time = 0  # The time based on the current clock speed.
        self._true_time = 0  # This always ticks at a clock speed of 1. Basically the true run time.
        self._frame_time = 0  # the total number of frames
        self._delta_time = 0  # delta_time of last update

    def tick(self, delta_time: 1/120):
        self._true_time += delta_time
        self._frame_time += 1

        self._delta_time = delta_time

        self._current_time += self.delta_time

    def length(self, time):
        return self.time - time if time >= 0 else 0

    def raw_length(self, raw_time):
        return self.raw_time - raw_time if raw_time >= 0 else 0

    @property
    def delta_time(self):
        return self._delta_time * self._speed

    @property
    def raw_delta_time(self):
        return self._delta_time

    @property
    def time(self):
        return self._current_time

    @property
    def raw_time(self):
        return self._true_time

    @property
    def frame(self):
        return self._frame_time

    @property
    def game_speed(self):
        return self._speed

    def set_game_speed(self, speed: float = 1.0):
        self._speed = speed


Clock = _Clock(clock_speed, update_rate)