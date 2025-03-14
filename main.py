# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from pygame.locals import *
from constants import *

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print('Starting Asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0)) 
        pygame.display.flip()
        Clock.tick(60)
        dt = Clock.tick(60)/1000

if __name__ == "__main__":
    main()