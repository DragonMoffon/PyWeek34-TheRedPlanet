from src.constants import normalise, lerp
from src.clock import Clock

from src.animations import Animator

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.map.map import Map


class PlayerMovement:

    def __init__(self, target, data, animator, _map):
        self.data = data
        self._target = target
        self._animator: Animator = animator
        self._map: Map = _map

        self.velocity = (0, 0)
        self.direction = (0, 0)

        self.speed = 0

        self.acceleration = data['acceleration']
        self.max_speed = data['max speed']
        self.sprint_modifier = data['sprint mod']

    def update(self, input_direction, sprint):
        self.direction = normalise(input_direction)

        _speed = self.max_speed * max(1, sprint*self.sprint_modifier)
        _target_speed = self.direction[0] * _speed, self.direction[1] * _speed

        self.velocity = lerp(self.velocity, _target_speed, self.acceleration)

        self._target.position = (self._target.center_x + self.velocity[0]*Clock.delta_time,
                                 self._target.center_y + self.velocity[1]*Clock.delta_time)

        if self._map.room.hit_walls(self._target):
            self._target.position = (self._target.center_x - self.velocity[0]*Clock.delta_time,
                                     self._target.center_y - self.velocity[1]*Clock.delta_time)
            self.velocity = (0, 0)
