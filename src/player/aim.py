from arcade import Sprite, load_texture

from src.constants import normalise, vec_angle
from src.input import Input


class Aim:

    def __init__(self, target):
        self._target = target
        self._direction = (0, 0)

        self._dist = 14*6

        self._arrow_sprite = Sprite(texture=load_texture(":data:/textures/arrow_placeholder.png"))

    def update(self):
        _p_pos = self._target.position
        _mouse_dir = normalise((Input.mouse[0] - _p_pos[0], Input.mouse[1] - _p_pos[1]))

        self._arrow_sprite.position = (_p_pos[0] + _mouse_dir[0]*self._dist, _p_pos[1] + _mouse_dir[1]*self._dist)
        # self._arrow_sprite.angle = vec_angle(_mouse_dir)

        self._direction = _mouse_dir

    @property
    def sprite(self):
        return self._arrow_sprite

    @property
    def direction(self):
        return self._direction

