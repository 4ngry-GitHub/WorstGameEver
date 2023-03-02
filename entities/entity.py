from abc import ABC, abstractmethod
from random import choice

import pygame

from config import config

class BaseEntity(ABC):
    
    @abstractmethod
    def foo() -> None:
        """TODO implement this later"""
        pass


class Cube:
    _surface = None
    _coordinates: tuple
    _speed: list
    _color = None
    rand_colors: tuple = ((255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 153, 51), (102, 0, 102))

    def __init__(
                    self, surface = pygame.Surface((20, 20)),
                    color: tuple = (255, 255, 255),
                    coordinates: tuple = (100, 100),
                    speed: list = [2, 2],
                ) -> None:
        self._surface = surface
        self._surface.fill(color)
        self._coordinates = coordinates
        self._speed = speed
        self._rectangle = self._surface.get_rect()

    @property
    def coordinates(self) -> tuple:
        return self._coordinates
    
    @property
    def surface(self):
        return self._surface
    
    @property
    def rectangle(self):
        return self._rectangle

    def move(self) -> None:
        self._rectangle = self._rectangle.move(self._speed)
        if self._rectangle.bottom >= config.window_height or self._rectangle.top <= 0:
            self._speed[1] = -self._speed[1]
            self.change_color_randor()

        if self._rectangle.right >= config.window_width or self._rectangle.right <= 0:
            self._speed[0] = -self._speed[0]
            self.change_color_randor()
    
    def change_color_randor(self) -> None:
        self._surface.fill(choice(self.rand_colors))