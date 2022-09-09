from typing import List

from arcade import Sprite, SpriteList, load_texture

from src.clock import Clock
from src.input import Input

from src.player.aim import Aim


from src.weapons.bullets import Bullet, SimpleBullet


class GunManager:

    def __init__(self, target, aim):
        self._aim: Aim = aim
        self._target: Sprite = target

        self._bullet_src = SimpleBullet
        self._bullets: List[Bullet] = []
        self._bullet_sprites = SpriteList()

        self._last_shot = Clock.time

    @property
    def bullets(self):
        return self._bullet_sprites

    def _shoot(self):
        _dir = self._aim.direction
        dx, dy = _dir[0] * 460, _dir[1] * 460
        x, y = self._target.position

        _bullet = self._bullet_src(x, y, dx, dy, self._bullets)
        self._bullets.append(_bullet)
        self._bullet_sprites.append(_bullet.sprite)

    def clear_bullets(self):
        self._bullets.clear()
        self._bullet_sprites.clear(deep=True)

    def bullets_hit(self, other: Sprite):
        struck = other.collides_with_list(self._bullet_sprites)
        for bullet in struck:
            bullet_idx = self._bullet_sprites.index(bullet)
            self._bullets[bullet_idx].kill()
        return bool(struck)

    def update(self):
        if Input['Fire'] and Clock.length(self._last_shot) >= 2/3:
            self._last_shot = Clock.time
            self._shoot()

        for bullet in self._bullets:
            bullet.update()

    def draw(self):
        self._bullet_sprites.draw(pixelated=True)

