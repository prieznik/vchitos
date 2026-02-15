# entity.py
import pygame
import random

WIDTH, HEIGHT = 600, 400

class Entity:
    def __init__(self, radius, color, speed):
        # Common attributes
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)
        self.radius = radius
        self.color = color
        self.speed = speed
        
        # Common velocity logic
        self.vel_x = random.choice([-self.speed, self.speed])
        self.vel_y = random.choice([-self.speed, self.speed])

    def move(self):
        """Standard movement and wall bounce for all entities."""
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.vel_x *= -1
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.vel_y *= -1

    def draw(self, surface):
        """Standard rendering."""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)