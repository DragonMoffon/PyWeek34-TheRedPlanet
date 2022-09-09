from arcade import Sprite


class Data:

    def __init__(self, data):
        self._health = data['health']
        self._speed = data['speed']

        self._weapon = data['weapon']

        self._sprite = Sprite(scale=4.0)

    @property
    def sprite(self):
        return self._sprite

    @property
    def position(self):
        return self._sprite.position

    @position.setter
    def position(self, pos):
        self._sprite.position = pos

    @property
    def velocity(self):
        return self._sprite.velocity

    @velocity.setter
    def velocity(self, vel):
        self._sprite.velocity = vel

    @property
    def speed(self):
        return self._speed

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health -= 1
