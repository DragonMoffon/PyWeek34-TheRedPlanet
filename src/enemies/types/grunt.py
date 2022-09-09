from arcade import load_texture

from src.clock import Clock
from src.constants import normalise, lerp

from src.player import PLAYER

from src.enemies.types.ai import Ai
from src.enemies.types.enemy import Enemy
from src.enemies.types.data import Data


class GruntData(Data):
    name: str = "grunt"

    def __init__(self, data):
        super().__init__(data)


class GruntAi(Ai):

    def __init__(self, data):
        super().__init__(data)

    def step(self):
        # TODO: Proper pathfinding using a* and includes avoiding other enemies.
        p_pos = PLAYER.position
        pos = self._data.position
        dir_e = normalise((pos[0]-p_pos[0], pos[1]-p_pos[1]))

        self._target_position = p_pos[0] + dir_e[0]*150, p_pos[1] + dir_e[1]*150
        target_pos = self._target_position

        t_dist = abs(pos[0] - target_pos[0]), abs(pos[1] - target_pos[1])

        dir_check = (round(-dir_e[0]), round(-dir_e[1]))

        if dir_check[0] < 0 and t_dist[0] > 25:
            self._input_target['Down'].press()
            self._input_target['Up'].release()
        elif dir_check[0] > 0 and t_dist[0] > 25:
            self._input_target['Up'].press()
            self._input_target['Down'].release()
        else:
            self._input_target['Up'].release()
            self._input_target['Down'].release()

        if dir_check[1] < 0 and t_dist[1] > 25:
            self._input_target['Left'].press()
            self._input_target['Right'].release()
        elif dir_check[1] > 0 and t_dist[1] > 25:
            self._input_target['Right'].press()
            self._input_target['Left'].release()
        else:
            self._input_target['Right'].release()
            self._input_target['Left'].release()


class Grunt(Enemy):

    def __init__(self):
        data = GruntData({'health': 4, 'speed': 300, 'weapon': None})
        super().__init__(GruntAi(data), data)
        self._data.sprite.texture = load_texture(":data:/textures/enemies.png", width=32, height=32)
        self._data.sprite.position = (200, 200)
        self._data.sprite.scale = 4.0

    def update(self):
        vel = normalise((self._ai.Input['Up'] - self._ai.Input['Down'],
                         self._ai.Input['Right'] - self._ai.Input['Left']))

        vel = (vel[0]*self._data.speed, vel[1]*self._data.speed)
        self._data.velocity = vel

        pos = self._data.position
        self._data.position = pos[0] + vel[0]*Clock.delta_time, pos[1] + vel[1]*Clock.delta_time

