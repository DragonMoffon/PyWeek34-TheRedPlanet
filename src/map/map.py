from random import choice

from src.map.room import Room, ROOM_SHELLS
from src.map.door import Door


OPP_DOORS = {'l': 'r', 'r': 'l', 't': 'b', 'b': 't'}


class Map:

    def __init__(self):
        self._current_room: Room = None
        self._last_door = 'l'
        self.rooms = []

    @property
    def room(self):
        return self._current_room

    def first_room(self, diff, thresh):
        next_room = ROOM_SHELLS['l']['r']
        self._last_door = 'l'
        self._current_room = next_room.generate_room(diff, thresh)
        self.rooms.append(next_room)

    def generate_room(self, door_direction, diff, thresh):
        next_room = choice(tuple(ROOM_SHELLS[door_direction].values()))
        self._last_door = door_direction
        self._current_room = next_room.generate_room(diff, thresh)
        self.rooms.append(next_room)

    def generate_doors(self):
        return tuple(Door(room, self._current_room.door_pos(room))
                     for room in self._current_room.doors if room != self._last_door)

    def draw(self):
        self._current_room.draw()

    def top_draw(self):
        self._current_room.top_draw()