from typing import Dict, Tuple

from arcade import load_texture, Texture, Sprite

from src.clock import Clock


def load_animation_set(src: str, animation_data: Tuple[Tuple[str, int, int], ...], frame_size: Tuple[int, int]):
    return {name: tuple(load_texture(src, frame_size[0]*i, height,  *frame_size) for i in range(count))
            for name, count, height in animation_data}


class Animator:

    def __init__(self, animation_set: Dict[str, Tuple[Texture, ...]], target: Sprite, animation_speed: float = 1/6):
        self._target: Sprite = target

        self._animations: Dict[str, Tuple[Texture, ...]] = animation_set

        self._speed: float = animation_speed

        self._frame_time: float = Clock.time
        self._current_frame: int = 0
        self._current_direction: int = 1

        self._current_animation: str = "idle"

        target.texture = self._animations[self._current_animation][self._current_frame]

    def update(self):
        if Clock.length(self._frame_time) > self._speed:
            self._current_frame = (self._current_frame + 1) % len(self._animations[self._current_animation])
            self._frame_time = Clock.time

            self._target.texture = self._animations[self._current_animation][self._current_frame]
            self._target.width = abs(self._target.width) * self._current_direction

    def set_animation(self, animation):
        self._current_animation = animation

    def set_direction(self, direction):
        if direction:
            self._current_direction = direction / abs(direction)
            self._target.width = abs(self._target.width) * self._current_direction
