from json import load

from arcade import Sprite, load_texture, SpriteList
from arcade.resources import resolve_resource_path

from src.input import Input
from src.clock import Clock

from src.animations import Animator, load_animation_set

from src.player.movement import PlayerMovement
from src.player.aim import Aim
from src.player.gun_manager import GunManager


class PlayerManager:

    def __init__(self):
        self._data = None

        self._body_sprite: Sprite = None
        self._animator: Animator = None

        self._aim: Aim = None
        self._gun_manager: GunManager = None

        self._sprite_list = SpriteList(lazy=True)

        self._player_movement: PlayerMovement = None

    def initialise(self, _map):
        with open(resolve_resource_path(":data:/player_data.json")) as data_file:
            self._data = load(data_file)

        self._body_sprite = Sprite(scale=4.0)
        _animations = (('idle', 1, 0), ('reload', 5, 32), ('run', 4, 64),
                       ('idleshoot', 4, 96), ('runshoot', 4, 128), ('die', 7, 160))
        self._animator = Animator(load_animation_set(":data:/textures/player.png", _animations, (32, 32)),
                                  self._body_sprite)
        self._body_sprite.hit_box = ((-8, -16), (-4, -8), (4, -8), (8, -16))

        self._aim = Aim(self._body_sprite)
        self._gun_manager = GunManager(self._body_sprite, self._aim)

        self._sprite_list.extend((self._body_sprite, self._aim.sprite))

        self._player_movement = PlayerMovement(self._body_sprite, self._data['move_data'], self._animator, _map)

    @property
    def position(self):
        return self._body_sprite.position

    @property
    def bullets(self):
        return self._gun_manager.bullets

    def hit_player(self, other):
        return self._body_sprite.collides_with_sprite(other)

    def list_hit_player(self, other):
        return self._body_sprite.collides_with_list(other)

    def bullets_hit(self, other):
        return self._gun_manager.bullets_hit(other)

    def place(self, x, y):
        self._body_sprite.position = (x, y)

    def clear_bullets(self):
        self._gun_manager.clear_bullets()

    def mission_update(self):
        vertical = Input['Up'] - Input['Down']
        horizontal = Input['Right'] - Input['Left']

        self._player_movement.update((horizontal, vertical), Input['Sprint'])
        self._aim.update()
        self._gun_manager.update()

        self._animator.set_direction(self._aim.direction[0])

        if self._player_movement.velocity[0] or self._player_movement.velocity[1]:
            _anim = 'run'
        else:
            _anim = 'idle'

        if Input['Fire']:
            _anim += 'shoot'

        self._animator.set_animation(_anim)
        self._animator.update()

    def draw(self):
        self._sprite_list.draw(pixelated=True)
        self._gun_manager.draw()
        self._body_sprite.draw_hit_box(line_thickness=4)
