import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity *dt

    def Collision(self, CircleShape):
        return super().Collision(CircleShape)

    def Split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        if ASTEROID_MIN_RADIUS <= self.radius <= ASTEROID_MAX_RADIUS:
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            child_asteroid_1 = Asteroid(self.position.x, self.position.y,new_radius)
            child_asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2

            child_asteroid_2 = Asteroid(self.position.x, self.position.y,new_radius)
            child_asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2

