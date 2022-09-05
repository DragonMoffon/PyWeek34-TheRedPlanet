from arcade import Texture, load_texture, Sprite

from src.clock import Clock


class Bullet:

    def __init__(self, _pos, _vel, _data, _parent=None):
        self._sprite = Sprite(_data['texture'])
        self._class = _data['class']

        self._pos = _pos
        self._vel = _vel

        self._sprite.position = _pos
        self._sprite.velocity = _vel

        self._spawn_time = Clock.time
        self._life_time = _data['life_time']

        self._parent = _parent

    @property
    def sprite(self):
        return self._sprite

    def _decay(self):
        if Clock.length(self._spawn_time) > self._life_time:
            self._destroy()

    def _destroy(self):
        pass

    def update(self):
        pass


class SimpleBullet(Bullet):

    def __init__(self, x, y, dx, dy):
        super().__init__((x, y), (dx, dy),
                         {'texture': load_texture(':data:/textures/bullet_placeholder.png'),
                          'class': 'simple',
                          'life_time': 12.0})

    def _destroy(self):
        self.sprite.remove_from_sprite_lists()
        self._parent.remove(self)

    def update(self):
        _pos = self._sprite.position
        _pos = _pos[0]+self._vel[0]*Clock.delta_time, _pos[1]+self._vel[1]*Clock.delta_time

        self.sprite.position = _pos
        self._decay()
