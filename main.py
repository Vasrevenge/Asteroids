# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from pygame.locals import *
from constants import *
from player import Player

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2),PLAYER_RADIUS) #(SCREEN_WIDTH/2), (SCREEN_HEIGHT/2),PLAYER_RADIUS
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
        player.draw(screen)
        pygame.display.flip()
        Clock.tick(60)
        dt = Clock.tick(60)/1000
        player.update(dt)

if __name__ == "__main__":
    main()