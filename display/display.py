from typing import Tuple

from display.color import ColorBase, Color
from display.status import StatusBase, Status
from display.size import SizeBase, Size


class Display:
    color: ColorBase
    size: SizeBase
    status: StatusBase


    def __init__(self, size: SizeBase = Size(), color: ColorBase = Color(), status: StatusBase = Status()) -> None:
        self.size = size
        self.color = color
        self.status = status