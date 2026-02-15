import pygame
import random

WIDTH, HEIGHT = 600, 400

class Food:
    def __init__(self):
        # Random position for the food particle
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)
        self.radius = 5
        self.color = (0, 255, 0) # Green for energy

    def respawn(self):
        """Moves the food to a new random location when eaten."""
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)