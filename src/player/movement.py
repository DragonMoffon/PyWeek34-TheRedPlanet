from src.constants import normalise, lerp
from src.clock import Clock

from src.animations import Animator


class PlayerMovement:

    def __init__(self, targets, data, animator):
        self.data = data
        self._targets = targets
        self._animator: Animator = animator

        self.velocity = (0, 0)
        self.direction = (0, 0)

        self.speed = 0

        self.acceleration = data['acceleration']
        self.max_speed = data['max speed']
        self.sprint_modifier = data['sprint mod']

    def update(self, input_direction, sprint):
        self.direction = normalise(input_direction)

        _speed = self.max_speed * max(1, sprint*self.sprint_modifier)
        _target = self.direction[0] * _speed, self.direction[1] * _speed

        self.velocity = lerp(self.velocity, _target, self.acceleration)

        for _target in self._targets:
            _target.position = (_target.center_x + self.velocity[0]*Clock.delta_time,
                                _target.center_y + self.velocity[1]*Clock.delta_time)
