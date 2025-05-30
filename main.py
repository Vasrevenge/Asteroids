# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame

from constants import *
from player import Player
from Asteroid import Asteroid
from AsteroidField import AsteroidField
from Shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawables, updatables)
    Shot.containers = (shots, drawables, updatables)
    Asteroid.containers = (asteroids, drawables, updatables)
    AsteroidField.containers = (updatables)


    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2),PLAYER_RADIUS) #(SCREEN_WIDTH/2), (SCREEN_HEIGHT/2),PLAYER_RADIUS
    dt = 0

    asteroidfield = AsteroidField() 

    print('Starting Asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.Collision(player) is True:
                print('Game Over !')
                return
            
        for asteroid in asteroids:
            for shot in shots:
                if shot.Collision(asteroid) is True:
                    shot.kill()
                    asteroid.Split()

        screen.fill((0,0,0))

        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()
        Clock.tick(60)
        dt = Clock.tick(60)/1000

if __name__ == "__main__":
    main()