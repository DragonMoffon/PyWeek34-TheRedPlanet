from typing import Dict

from random import choice

from arcade.resources import resolve_resource_path

from pytiled_parser import parse_map, TiledMap
from arcade.tilemap import TileMap

from src.enemies.spawner import generate_round
from src.enemies.wave import Wave

ROOM_SHELLS: Dict[str, Dict[str, 'RoomShell']] = {'l': {}, 't': {}, 'b': {}}


def load_all_rooms():
    all_room_names = {'l': ('t', 'tr', 'tb', 'trb', 'r'),  # ('t', 'r', 'b', 'tb', 'tr', 'rb', 'trb'),
                      't': ('r', 'b', 'rb'), 'b': ('t', 'r', 'tr')}
    for entrance in all_room_names:
        for room in all_room_names[entrance]:
            ROOM_SHELLS[entrance][room] = RoomShell(f':data:/rooms/{entrance}-{room}.tmj')


class Room:

    def __init__(self, tiled_map: TileMap, wave_round: list, doors: dict = None):
        self._map = tiled_map

        self._walls = self._map.sprite_lists['Walls']
        self._floor = self._map.sprite_lists['Floor']

        self._round = wave_round

        self._doors = doors

    @property
    def round(self):
        return self._round

    @property
    def map(self):
        return self._map

    @property
    def doors(self):
        return self._doors

    @property
    def width(self):
        return self._map.width * self._map.tile_width * self._map.scaling

    @property
    def height(self):
        return self._map.height * self._map.tile_height * self._map.scaling

    def draw(self):
        self._floor.draw(pixelated=True)
        self._walls.draw(pixelated=True)

    def door_pos(self, door_id):
        door_pos = self._doors[door_id]
        return ((door_pos[0]+0.5)*self._map.tile_width*self._map.scaling,
                (self._map.height-(door_pos[1]-0.5))*self._map.tile_height*self._map.scaling)


class RoomShell:

    def __init__(self, room_src: str):
        self._map: TiledMap = parse_map(resolve_resource_path(room_src))
        self._layers = {}
        for layer in self._map.layers[:]:
            if layer.name == "Doors":
                _tile_size = self._map.tile_size
                self._layers[layer.name] = {_l.properties['location']: (_l.coordinates[0]//_tile_size[0],
                                                                        _l.coordinates[1]//_tile_size[1])
                                            for _l in layer.tiled_objects}
                self._map.layers.remove(layer)
            else:
                self._layers[layer.name] = layer.data

    def generate_room(self, diff, thresh):
        return Room(TileMap(tiled_map=self._map, scaling=4.0), generate_round(diff, thresh),
                    self._layers['Doors'])
