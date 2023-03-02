from abc import ABC, abstractmethod

from config import config

class SizeBase(ABC):

    @abstractmethod
    def get_size(self) -> tuple:
        """Get size in tuple(width, heigth)"""
        pass


class Size(SizeBase):
    _height: int
    _width: int

    def __init__(self, width = config.window_width, height = config.window_height) -> None:
        self._width = width
        self._height = height

    def get_size(self) -> tuple:
        return (self._width, self._height)
    