from abc import ABC, abstractmethod

from loguru import logger

class ColorBase(ABC):

    @abstractmethod
    def get_color(self) -> tuple:
        """Returning color in tuple RGB. Example: (255,255,255)"""
        pass


class Color(ColorBase):
    _red_channel: int = 0
    _green_channel: int = 0
    _blue_channel: int = 0
    _color: tuple

    def __init__(self, color: tuple = (0, 0, 0), red: int = 0, green: int = 0, blue: int = 0) -> None:
        self._color = color
        self._red_channel = red
        self._green_channel = green
        self._blue_channel = blue

    def get_color(self) -> tuple:
        return self._color
    
    def set_color(self, color: tuple) -> None:
        if isinstance(color, tuple) and len(color) == 3:
            self._color = color
        logger.error("Incorrect type or len of rgb_tuple")
        raise ValueError("Wrongs values in color. Supposed to be a tuple of ints(255,255,255) and contain 3 elemets.")
    
    