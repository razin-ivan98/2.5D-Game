from typing import List
import numpy
import pygame
from pygame import Surface, Color



class Drawer:
    def __init__(self):
        pygame.init()
        self.__screen_width = 0
        self.__screen_height = 0
        self.__screen: Surface = None
        self.__clear_color = Color(0, 0, 0)
        self.frame = None
        # self.__surarray: ndarray = None

    def create_window(self, width: int, height: int, title: str):
        pygame.init()
        self.__screen_width = width
        self.__screen_height = height
        self.__screen = pygame.display.set_mode([width, height])
        # self.__surarray = pygame.surfarray.pixels3d(self.__screen)
        self.frame = numpy.random.uniform(0, 1, (self.__screen_width, self.__screen_height, 3))
        pygame.display.set_caption(title)

    def clear(self):
        self.__screen.fill(self.__clear_color)


    def set_pixel(self, x: int, y: int, color):
        self.__screen.set_at([x, y], color)
        # self.__pixels_array[x, y] = pygame.Color(color)
        # self.__surarray[x, y] = color
        # self.frame[x, y] = color
        pass

    def update(self):
        # dist_rect = self.__dist_image.get_rect(center=pygame.mouse.get_pos())
        # dist_rect = self.__dist_image.get_rect(center=pygame.mouse.get_pos())
        # self.__screen.unlock()
        # self.__dist_image.unlock()
        # surface = pygame.surfarray.make_surface(self.__surarray)
        # self.__screen.blit(surface, (0, 0))
        # self.__screen.fill(self.__clear_color)
        # surf = pygame.surfarray.make_surface(self.frame * 255)
        # surf = pygame.transform.scale(surf, (self.__screen_width, self.__screen_height))
        # self.__screen.blit(surf, (0, 0))
        pygame.display.update()

    @property
    def width(self):
        return self.__screen_width

    @property
    def height(self):
        return self.__screen_height
