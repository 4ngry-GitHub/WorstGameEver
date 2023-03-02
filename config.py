from dataclasses import dataclass


@dataclass
class Config:
    window_width: int = 800
    window_height: int = 600


config = Config()
