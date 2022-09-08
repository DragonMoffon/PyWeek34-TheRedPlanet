from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.engine import _Engine

from arcade import View, Camera, draw_point
from arcade.color import RADICAL_RED, BLUE
from arcade.background import Background

from src.input import Input
from src.clock import Clock

from src.player import PLAYER

from src.enemies.manager import EnemyManager

from src.map.map import Map, OPP_DOORS


class MissionView(View):

    def __init__(self, engine: '_Engine'):
        super().__init__(engine)
        self._engine: '_Engine' = engine
        self._camera = Camera(engine.width, engine.height, engine)

        self._map: Map = Map()

        self._enemy_manager: EnemyManager = EnemyManager(self._map)

        self._doors = ()

    def begin(self):
        self._map.first_room(*self._enemy_manager.next_room_diff)
        self._doors = ()

        # self._enemy_manager.enter_room(self._map.room)
        PLAYER.place(*self._map.room.door_pos('l'))

    def enter_door(self, door):
        direction = OPP_DOORS[door.direction]
        self._map.generate_room(direction, *self._enemy_manager.next_room_diff)
        self._doors = ()

        PLAYER.place(*self._map.room.door_pos(direction))
        self._camera.move_to((-self._map.room.width // 2, -self._map.room.height // 2), 1.0)

    def on_update(self, delta_time):
        Clock.tick(delta_time)
        Input.update_camera_pos(self._camera.position)

        PLAYER.mission_update()

        _p_pos = PLAYER.position
        camera_x = -(self._camera.viewport_width - self._map.room.width) // 2
        if self._engine.width < self._map.room.width:
            camera_x = min(max(int(PLAYER.position[0] - self._camera.viewport_width//2), 0),
                           self._map.room.width - self._camera.viewport_width)
        camera_y = -(self._camera.viewport_height - self._map.room.height) // 2
        if self._engine.height < self._map.room.height:
            camera_y = min(max(int(PLAYER.position[1] - self._camera.viewport_height//2), 0),
                           self._map.room.height-self._camera.viewport_height)
        self._camera.move_to((camera_x, camera_y), 0.6)
        # print(self._map.room.width, self._map.room.height)

        self._enemy_manager.update()

        if self._enemy_manager.cleared_room and not self._doors:
            self._doors = ()
            self._doors = self._map.generate_doors()
        else:
            for door in self._doors:
                if door.player_touching():
                    self.enter_door(door)
                    break

    def on_draw(self):
        self.clear()
        self._camera.use()

        self._map.draw()
        self._enemy_manager.draw()
        PLAYER.draw()

        for door in self._doors:
            door.draw()



    def on_show_view(self):
        pass
        # self._camera.zoom(2.0)
