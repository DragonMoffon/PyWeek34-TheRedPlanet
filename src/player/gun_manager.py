from arcade import Sprite, SpriteList, load_texture

from src.clock import Clock
from src.input import Input

from src.player.aim import Aim


class Bullet(Sprite):

    def __init__(self, x, y, dx, dy):
        super().__init__(texture=load_texture(":data:/textures/bullet_placeholder.png"))
        self.position = (x, y)
        self.velocity = (dx, dy)

        self._start = Clock.time

    def update(self):
        self.position = (self.center_x + self.velocity[0]*Clock.delta_time,
                         self.center_y + self.velocity[1]*Clock.delta_time)

        if Clock.length(self._start) > 12.0:
            self.remove_from_sprite_lists()


class GunManager:

    def __init__(self, target, aim):
        self._aim: Aim = aim
        self._target: Sprite = target

        self._bullet_src = Bullet
        self._bullets = SpriteList()

        self._last_shot = Clock.time

    def _shoot(self):
        _dir = self._aim.direction
        dx, dy = _dir[0] * 460, _dir[1] * 460
        x, y = self._target.position

        _bullet = self._bullet_src(x, y, dx, dy)
        self._bullets.append(_bullet)

    def update(self):
        if Input['Fire'] and Clock.length(self._last_shot) >= 0.1:
            self._last_shot = Clock.time
            self._shoot()
        self._bullets.update()

    def draw(self):
        self._bullets.draw(pixelated=True)

