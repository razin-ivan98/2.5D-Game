from Map import Map
from MapLoader import load_map
from Player import Player
from Renderer.Renderer import Renderer
from Vector2 import Vector2
from Drawer import Drawer
from Input import Input, EXIT


class Game:
    def __init__(self, drawer: Drawer, game_input: Input):
        self.__map = Map(load_map("./maps/map.txt"))
        self.__player = Player(Vector2(3, 6), self.__map)
        self.__drawer = drawer
        self.__game_input = game_input
        self.__renderer = Renderer(drawer, self.__map)

    def update(self, delta_seconds: float) -> bool:
        self.__game_input.tick()
        if self.__game_input.has_event(EXIT):
            return False

        self.__drawer.clear()

        movement = self.__game_input.get_movement_axis() * delta_seconds
        self.__player.go(movement)

        self.__renderer.render(self.__player.position, self.__player.direction)
        self.__drawer.update()
        return True
