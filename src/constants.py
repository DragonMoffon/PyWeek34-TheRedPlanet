from math import sqrt, atan2, degrees

clock_speed = 1
update_rate = 1/60  # The update speed of the game. At 1/120 the engine will try run at 120 fps.
draw_rate = 1/60  # The draw speed of the game. At 1/120 the engine will try draw at 120 fps.

screen_width = 800
screen_height = 600


def normalise(vec):
    _length = sqrt(sum(v**2 for v in vec)) or 1
    return tuple(v / _length for v in vec)


def clamp(vec, length):
    _length = sqrt(sum(v**2 for v in vec)) or 1
    return tuple(v / _length * length for v in vec)


def lerp(vec_1, vec_2, a):
    return tuple(_1 + a * (_2 - _1) for _1, _2 in zip(vec_1, vec_2))


def vec_radians(vec):
    return atan2(vec[1], vec[0])


def vec_angle(vec):
    return degrees(vec_radians(vec))


def dot(vec_1, vec_2):
    return sum(map(lambda a, b: a*b, zip(vec_1, vec_2)))
