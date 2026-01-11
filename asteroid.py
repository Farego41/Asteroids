import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            first_vector = self.velocity.rotate(random_angle)
            second_vector = self.velocity.rotate(-random_angle)
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_ast1 = Asteroid(self.position[0], self.position[1], self.new_radius)
            new_ast2 = Asteroid(self.position[0], self.position[1], self.new_radius)
            new_ast1.velocity = first_vector * 1.2
            new_ast2.velocity = second_vector * 1.2