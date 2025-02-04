import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y,  SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                            (int(self.position.x), int(self.position.y)), SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt