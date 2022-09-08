from arcade import Sprite, load_texture, draw_text

from src.clock import Clock

from src.player import PLAYER


class Door:

    def __init__(self, direction, position):
        self._direction = direction

        self._hitbox_sprite = Sprite(":data:/textures/collision_box.png", scale=4.0, hit_box_algorithm='Simple',
                                     center_x=position[0], center_y=position[1])
        self._flicker_time = 0
        self._frame = 0

        if direction == 't':
            self._hitbox_sprite.angle = 90
            self._continue_textures = (load_texture(":data:/textures/continue.png", width=48, height=48),
                                       load_texture(":data:/textures/continue.png", x=48, width=48, height=48))
            self._continue_sprite = Sprite(texture=self._continue_textures[0], scale=4.0,
                                           center_x=position[0], center_y=position[1] - 32 * 5)
        elif direction == "r":
            self._continue_textures = (load_texture(":data:/textures/continue.png", y=48, width=48, height=48),
                                       load_texture(":data:/textures/continue.png", x=48, y=48, width=48, height=48))
            self._continue_sprite = Sprite(texture=self._continue_textures[0], scale=4.0,
                                           center_x=position[0] - 48 * 4, center_y=position[1])
        elif direction == "b":
            self._hitbox_sprite.angle = -90
            self._continue_textures = (load_texture(":data:/textures/continue.png", y=96, width=48, height=48),
                                       load_texture(":data:/textures/continue.png", x=48, y=96, width=48, height=48))
            self._continue_sprite = Sprite(texture=self._continue_textures[0], scale=4.0,
                                           center_x=position[0], center_y=position[1] + 32 * 5)
        else:
            raise ValueError("Can't enter that door bro")

    @property
    def direction(self):
        return self._direction

    def draw(self):
        if Clock.length(self._flicker_time) > 1/3:
            self._flicker_time = Clock.time
            self._frame = (1 - self._frame)
            self._continue_sprite.texture = self._continue_textures[self._frame]

        # self._hitbox_sprite.draw(pixelated=True)
        self._continue_sprite.draw(pixelated=True)

    def player_touching(self):
        return PLAYER.hit_player(self._hitbox_sprite)
