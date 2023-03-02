from dataclasses import dataclass


@dataclass
class Colors:
    red: tuple = (255, 0, 0)
    green: tuple = (0, 255, 0)
    blue: tuple = (0, 0, 255)
    orange: tuple = (255, 153, 51)
    purple: tuple = (102, 0, 102)
