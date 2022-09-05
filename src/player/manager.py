from json import load

from arcade import Sprite, load_texture, SpriteList
from arcade.resources import resolve_resource_path

from src.input import Input
from src.clock import Clock

from src.player.movement import PlayerMovement
from src.player.aim import Aim
from src.player.gun_manager import GunManager


class PlayerManager:

    def __init__(self):
        with open(resolve_resource_path(":data:/player_data.json")) as data_file:
            self._data = load(data_file)

        self._body_sprite = Sprite(texture=load_texture(":data:/textures/player_placeholder_2.png"))

        self._aim = Aim(self._body_sprite)
        self._shooting = GunManager(self._body_sprite, self._aim)

        _sprites = (self._body_sprite,)

        self._sprite_list = SpriteList()
        self._sprite_list.extend(_sprites + (self._aim.sprite,))

        self._player_movement = PlayerMovement(_sprites, self._data['move_data'])

    def place_player(self, x, y):
        self._body_sprite.position = (x, y)

    def mission_update(self):
        vertical = Input['Up'] - Input['Down']
        horizontal = Input['Right'] - Input['Left']

        self._player_movement.update((horizontal, vertical))
        self._aim.update()
        self._shooting.update()

    def draw(self):
        self._sprite_list.draw(pixelated=True)
        self._shooting.draw()
