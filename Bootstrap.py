from Drawer import Drawer
from Game import Game
from GameCycle import GameCycle
from Input import Input

WIDTH = 700
HEIGHT = 700
TITLE = "Game"


class Bootstrap:
    def __init__(self):
        self.__drawer = Drawer()
        self.__drawer.create_window(WIDTH, HEIGHT, TITLE)

        self.__game_input = Input()
        self.__game_cycle = GameCycle()
        self.__game = Game(self.__drawer, self.__game_input)

        self.__game_cycle.start_loop(self.__game.update)
