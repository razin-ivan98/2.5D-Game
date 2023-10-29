from typing import List
from Vector2 import Vector2

WALL = "#"


class Map:
    def __init__(self, map: List[str]):
        self.__map = map

    def can_move_to(self, position: Vector2):
        i = int(position.x)
        j = int(position.y)
        return self.__map[j][i] != WALL

    def is_renderable(self, position: Vector2):
        i = int(position.x)
        j = int(position.y)
        return self.__map[j][i] == WALL
