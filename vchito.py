# vchito.py
import pygame
import random

# Global constants for the environment
WIDTH, HEIGHT = 600, 400

class Vchito:
    """
    Class representing a 'Vchito' entity.
    All instances share the same basic behavior and size.
    """
    def __init__(self):
        # Initial position: random point within the screen boundaries
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)
        
        # Physical characteristics
        self.radius = 15
        self.color = (0, 255, 255)  # Cyan neon color
        
        # Velocity: random direction but constant speed magnitude
        self.vel_x = random.choice([-1, 1])
        self.vel_y = random.choice([-1, 1])

    def move(self):
        """Updates position and handles wall collisions."""
        self.x += self.vel_x
        self.y += self.vel_y

        # Bounce logic for horizontal walls (Left/Right)
        if self.x + self.radius >= WIDTH or self.x - self.radius <= 0:
            self.vel_x *= -1
            
        # Bounce logic for vertical walls (Top/Bottom)
        if self.y + self.radius >= HEIGHT or self.y - self.radius <= 0:
            self.vel_y *= -1

    def draw(self, surface):
        """Renders the Vchito on the provided Pygame surface."""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)