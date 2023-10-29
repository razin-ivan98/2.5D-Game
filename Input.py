from typing import List

import pygame
from pygame.event import Event
from pygame.key import ScancodeWrapper

EXIT = "exit"
ATTACK = "attack"
ACT = "act"

GO_FORWARD = "go_forward"
GO_BACK = "go_back"
GO_LEFT = "go_left"
GO_RIGHT = "go_tight"

VIEW_AXIS = "view_axis"
WALK_AXIS = "walk_axis"


_CONTROL_KEYS = {
    ATTACK: pygame.K_KP_ENTER,
    EXIT: pygame.K_ESCAPE,
    ACT: pygame.K_e,
    GO_FORWARD: pygame.K_w,
    GO_BACK: pygame.K_s,
    GO_LEFT: pygame.K_a,
    GO_RIGHT: pygame.K_d
}


class Input:
    def __init__(self):
        self.__events: List[Event] = []
        self.__pressed: ScancodeWrapper = None

    def tick(self):
        self.__events = pygame.event.get()
        self.__pressed = pygame.key.get_pressed()

    def has_event(self, event_type: str):
        for event in self.__events:
            if event.type == pygame.KEYDOWN and event.key == _CONTROL_KEYS[event_type]:
                return True
        return False

    def get_view_axis(self):
        view_axis = pygame.math.Vector2(0, 0)
        mouse_position = pygame.mouse.get_rel()
        view_axis.x += mouse_position[0]
        return view_axis

    def get_movement_axis(self):
        movement_axis = pygame.math.Vector2(0, 0)

        if self.__pressed[_CONTROL_KEYS[GO_FORWARD]]:
            movement_axis.y -= 1
        if self.__pressed[_CONTROL_KEYS[GO_BACK]]:
            movement_axis.y += 1
        if self.__pressed[_CONTROL_KEYS[GO_LEFT]]:
            movement_axis.x -= 1
        if self.__pressed[_CONTROL_KEYS[GO_RIGHT]]:
            movement_axis.x += 1

        return movement_axis
