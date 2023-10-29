import math
from Drawer import Drawer
from Renderer.RayCasting import cast
from Vector2 import Vector2
from Map import Map

STEP = 0.05
FOV = math.pi / 3

WALL_COLOR = [255, 255, 0]
OTHER_COLOR = [0, 0, 255]


class Renderer:
    def __init__(self, drawer: Drawer, map: Map):
        self.__drawer = drawer
        self.__map = map

    def __is_renderbale(self, x: float, y: float):
        return self.__map.is_renderable(Vector2(x, y))

    def render(self, camera_pos: Vector2, camera_direction: Vector2):
        rays_count = self.__drawer.width
        angle_step = FOV / rays_count
        normalized_camera_direction = camera_direction.normalize()

        first_ray_direction = normalized_camera_direction.rotate_rad(-FOV / 2)

        for x in range(rays_count):
            ray_direction = first_ray_direction.rotate_rad(angle_step * x)
            distance = cast([camera_pos.x, camera_pos.y], [ray_direction.x, ray_direction.y], self.__is_renderbale)

            wall_height = self.__drawer.height / distance
            self.__draw_column(x, wall_height)

    def __draw_column(self, x: int, wall_height):
        screen_height = self.__drawer.height
        floor = int(screen_height / 2 - wall_height / 2)
        ceiling = int(screen_height / 2 + wall_height / 2)

        for y in range(floor):
            self.__drawer.set_pixel(x, y, OTHER_COLOR)
        for y in range(floor, ceiling):
            self.__drawer.set_pixel(x, y, WALL_COLOR)
        for y in range(ceiling, screen_height):
            self.__drawer.set_pixel(x, y, OTHER_COLOR)

