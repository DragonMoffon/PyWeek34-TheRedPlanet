from src.constants import normalise, lerp
from src.clock import Clock


class PlayerMovement:

    def __init__(self, targets, data):
        self.data = data
        self._targets = targets

        self.velocity = (0, 0)
        self.direction = (0, 0)

        self.speed = 0

        self.acceleration = data['acceleration']
        self.max_speed = data['max speed']
        self.sprint_modifier = data['sprint mod']

    def update(self, input_direction):
        self.direction = normalise(input_direction)

        _target = self.direction[0] * self.max_speed, self.direction[1] * self.max_speed

        self.velocity = lerp(self.velocity, _target, self.acceleration)

        for _target in self._targets:
            _target.position = (_target.center_x + self.velocity[0]*Clock.delta_time,
                                _target.center_y + self.velocity[1]*Clock.delta_time)
