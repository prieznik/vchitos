# food.py
import pygame
import random

# Environment boundaries
WIDTH, HEIGHT = 600, 400

class Food:
    def __init__(self):
        self.radius = 5
        self.color = (0, 255, 0) # Green
        self.speed = 1.5 # Constant speed magnitude
        self.respawn()

    def respawn(self):
        """Resets food position and sets a new random constant velocity."""
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)
        
        # We give it a simple velocity, just like a Vchito
        self.vel_x = random.choice([-self.speed, self.speed])
        self.vel_y = random.choice([-self.speed, self.speed])

    def update(self):
        """Simple autonomous movement: Move and Bounce."""
        # 1. Update position based on velocity
        self.x += self.vel_x
        self.y += self.vel_y

        # 2. Wall collisions (Bouncing logic)
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.vel_x *= -1
            
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.vel_y *= -1

    def draw(self, surface):
        """Renders the food pellet on the screen."""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)