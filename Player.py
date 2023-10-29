from Map import Map
from Vector2 import Vector2


class Player:
    def __init__(self, position: Vector2, map: Map):
        self.__position = position
        self.__direction = Vector2(0, -1)
        self.__speed = 2
        self.__map = map

    def go(self, direction):
        new_position = self.__position + direction * self.__speed
        if self.__map.can_move_to(new_position):
            self.__position = new_position

    @property
    def position(self):
        return self.__position

    @property
    def direction(self):
        return self.__direction
