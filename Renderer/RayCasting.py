import math
from typing import Callable
from numba import njit

@njit
def __get_initial_map_coord(camera_pos: float):
    return int(camera_pos)

@njit
def __get_delta_dist(direction: float):
    return math.inf if direction == 0 else math.fabs(1 / direction)

@njit
def __get_step(direction: float):
    return direction / math.fabs(direction)

@njit
def __get_initial_dist_to_side(direction: float, position: float, dist_delta: float):
    map_coord = int(position)

    if direction < 0:
        return (position - map_coord) * dist_delta
    return (map_coord + 1 - position) * dist_delta

@njit
def cast(camera_pos: [int, int], direction: [int, int], is_hit: Callable[[float, float], bool]):
    map_x = __get_initial_map_coord(camera_pos.x)
    map_y = __get_initial_map_coord(camera_pos.y)

    x_delta_dist = __get_delta_dist(direction.x)
    y_delta_dist = __get_delta_dist(direction.y)

    x_step = __get_step(direction.x)
    y_step = __get_step(direction.y)

    x_dist_to_side = __get_initial_dist_to_side(direction.x, camera_pos.x, x_delta_dist)
    y_dist_to_side = __get_initial_dist_to_side(direction.y, camera_pos.y, y_delta_dist)

    hit = False
    hit_side = 0
    while not hit:
        if x_dist_to_side < y_dist_to_side:
            x_dist_to_side += x_delta_dist
            map_x += x_step
            hit_side = 0
        else:
            y_dist_to_side += y_delta_dist
            map_y += y_step
            hit_side = 1
        if is_hit(map_x, map_y):
            hit = True

    if hit_side == 0:
        wall_dist = x_dist_to_side - x_delta_dist
    else:
        wall_dist = y_dist_to_side - y_delta_dist

    return wall_dist
