import pygame
import random

# Global Environment Constants
WIDTH, HEIGHT = 600, 400

class Entity:
    """Base class for all simulation actors (Vchitos and Food)."""
    def __init__(self, radius, color, speed):
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)
        self.radius = radius
        self.color = color
        self.speed = speed
        
        # Initial random velocity
        self.vel_x = random.choice([-self.speed, self.speed])
        self.vel_y = random.choice([-self.speed, self.speed])

    def move(self):
        """Applies basic physics: movement and screen boundary bouncing."""
        self.x += self.vel_x
        self.y += self.vel_y

        # Screen collision (Horizontal)
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.vel_x *= -1
        # Screen collision (Vertical)
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.vel_y *= -1

    def draw(self, surface):
        """Renders the entity as a circle."""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))