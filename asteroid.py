import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        return pygame.draw.circle(
            screen, 
            "red", 
            self.position, 
            self.radius, 
            2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20.0, 50.0)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            vector_new = pygame.Vector2(0, 1) + self.velocity * 1.2
            
            asteroid_a = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_a.velocity = vector_new.rotate(random_angle)
            
            asteroid_b = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_b.velocity = vector_new.rotate(-random_angle)