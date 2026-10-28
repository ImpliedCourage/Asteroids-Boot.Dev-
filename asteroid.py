import pygame
import random

from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt: float) -> None:
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        rand_angle = random.uniform(20, 50)
        new_direction = self.velocity.rotate(rand_angle)
        self.radius -= ASTEROID_MIN_RADIUS

        new_asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        new_asteroid.velocity = new_direction * 1.2
        new_asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        new_asteroid.velocity = -new_direction * 1.2
