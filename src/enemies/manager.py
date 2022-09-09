from typing import List

from arcade import SpriteList

from src.map.room import Room
from src.enemies.wave import Wave

from src.enemies.types.enemy import Enemy

from src.player import PLAYER


class EnemyManager:

    def __init__(self, _map):
        self._current_round = []
        self._current_wave = None

        self._current_enemies: List[Enemy] = []
        self._enemy_sprites = SpriteList()

        self._map = _map

        self._difficulty = 5
        self._difficulty_threshold = 1

    @property
    def next_room_diff(self):
        return self._difficulty, self._difficulty_threshold

    @property
    def cleared_room(self):
        return not (len(self._current_round) or len(self._current_enemies))

    def enter_room(self, room: Room, door: str = 'l'):
        self._current_round = list(room.round)
        self._current_wave = Wave(self._current_round.pop(0), None)
        self._current_enemies = self._current_wave.enemies

        self._enemy_sprites.clear(True)
        self._enemy_sprites.extend(enemy.sprite for enemy in self._current_enemies)

    def update(self):
        for enemy in self._current_enemies:
            enemy.ai_step()

        for enemy in self._current_enemies:
            enemy.update()
            if enemy.health <= 0:
                self._current_enemies.remove(enemy)
                enemy.sprite.remove_from_sprite_lists()

    def collisions(self):
        for index, enemy in enumerate(self._current_enemies[:]):
            hit = PLAYER.bullets_hit(self._enemy_sprites[index])
            if hit:
                enemy.damage()

    def draw(self):
        self._enemy_sprites.draw(pixelated=True)
