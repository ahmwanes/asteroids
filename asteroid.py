import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand = random.uniform(20, 50)
        v1 = self.velocity.rotate(rand)
        v2 = self.velocity.rotate(-rand)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        astroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        astroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        astroid_1.velocity = v1 * 1.2
        astroid_2.velocity = v2 * 1.2
