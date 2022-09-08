from json import load
from typing import Dict

import arcade.key as keys
from arcade.resources import resolve_resource_path

from src.clock import Clock


class Key:

    def __init__(self, name):
        self._name = name

        self._pressed = False
        self._press_time = -1
        self._press_frame = -1
        self._release_frame = -1

    def __repr__(self):
        return f"{self._name} : {self._pressed}"

    def __sub__(self, other):
        return self._pressed - other._pressed

    def held(self, length):
        return length >= Clock.length(self._press_time)

    def __bool__(self):
        return self._pressed

    def press(self):
        if not self._pressed:
            self._press_time = Clock.time
            self._press_frame = Clock.frame

            self._release_frame = -1

        self._pressed = True

    def release(self):
        if self._pressed:
            self._release_frame = Clock.frame

            self._press_frame = -1
            self._press_time = -1

        self._pressed = False

    @property
    def pressed(self):
        return self._press_frame + 1 == Clock.frame

    @property
    def released(self):
        return self._release_frame + 1 == Clock.frame

    @property
    def length(self):
        return Clock.length(self._press_time)

    @property
    def name(self):
        return self._name

    def __mul__(self, other):
        return other * self._pressed

    def __add__(self, other):
        return other + self._pressed


class NullKey(Key):

    def press(self):
        pass

    def release(self):
        pass


def process_key_data():
    global Input
    _keys = {"mouse": {'left': 1, 'middle': 2, 'right': 4},
             "key": {'up': keys.UP, 'down': keys.DOWN, 'left': keys.LEFT, 'right': keys.RIGHT, 'esc': keys.ESCAPE,
                     'rshift': keys.LSHIFT, 'w': keys.W, 'a': keys.A, 's': keys.S, 'd': keys.D, 'r': keys.R}}

    with open(resolve_resource_path(":data:/key_data.json")) as _file:
        _key_json: dict = load(_file)
        _key_dict: dict = {}
        for key, item in _key_json.items():
            key = key.split("_")[0]
            item = item.split("_")
            if key not in _key_dict:
                _key = Key(key)
                _key_dict[key] = _key
            _key_dict[_keys[item[0]][item[1]]] = _key
    return _key_dict


class InputStream:

    def __init__(self):
        self._null_key = NullKey('null')
        self._key_data: Dict[Key] = None
        self._modifiers = 0
        self._mouse_pos = (0, 0)
        self._mouse_speed = (0, 0)

        self._camera_pos = (0, 0)

    def update_camera_pos(self, camera_pos):
        self._camera_pos = camera_pos

    def setup_keys(self):
        if not self._key_data:
            self._key_data = process_key_data()

    def __getitem__(self, item):
        return self._key_data.get(item, self._null_key)

    def key_press(self, key, modifiers):
        self[key].press()
        self._modifiers = modifiers

    def key_release(self, key, modifiers):
        self[key].release()
        self._modifiers = modifiers

    def update_mouse(self, x, y, dx=None, dy=None):
        self._mouse_pos = (x, y)
        self._mouse_speed = (dx, dy) if dx and dy else self._mouse_speed

    @property
    def mouse_raw(self):
        return self._mouse_pos

    @property
    def mouse(self):
        return self._camera_pos[0] + self._mouse_pos[0], self._camera_pos[1] + self._mouse_pos[1]


Input: InputStream = InputStream()

