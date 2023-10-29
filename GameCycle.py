from typing import Callable
from pygame import time
import pygame

FPS_UPDATE_TIMEOUT = 1000


class GameCycle:
    def __init__(self):
        self.__last_frame_time = self.get_milliseconds()
        self.__updater: Callable[[float], bool] = None
        self.__is_running = False
        self.__milliseconds_to_update_fps = FPS_UPDATE_TIMEOUT
        self.__frames_by_last_second = 0

    def start_loop(self, updater: Callable[[float], bool]):
        self.__updater = updater
        self.__is_running = True
        while self.__is_running:
            current_time = self.get_milliseconds()
            delta = current_time - self.__last_frame_time

            self.__milliseconds_to_update_fps -= delta
            if self.__milliseconds_to_update_fps <= 0:
                print("FPS: ", self.__frames_by_last_second)
                self.__milliseconds_to_update_fps = FPS_UPDATE_TIMEOUT
                self.__frames_by_last_second = 0

            delta_seconds = delta / 1000
            self.__is_running = self.__updater(delta_seconds)
            self.__last_frame_time = current_time
            self.__frames_by_last_second += 1
        pygame.quit()

    def get_milliseconds(self):
        return time.get_ticks()
