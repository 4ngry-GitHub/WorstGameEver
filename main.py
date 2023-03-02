import pygame
from loguru import logger

from display.display import Display
from entities.entity import Cube

pygame.init()
display = Display()
screen = display.size.get_size()
window = pygame.display.set_mode(screen)

cube = Cube()


def launch_game():
    while display.status.status:
        for event in pygame.event.get():
            if event == pygame.constants.QUIT:
                logger.info("Exiting with code 0.")
                display.status.switch_off()
        
        window.fill(display.color.get_color())
        # window.blit(cube.surface, cube.coordinates)
        window.blit(cube.surface, cube.rectangle)
        cube.move()
        pygame.display.flip()


if __name__ == "__main__":
    launch_game()