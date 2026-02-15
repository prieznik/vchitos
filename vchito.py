# vchito.py
import math
from Entity import Entity

class Vchito(Entity):
    def __init__(self):
        # Inherit from Entity: radius 15, cyan, speed 1.0 (or whatever you prefer)
        super().__init__(radius=15, color=(0, 255, 255), speed=1.0)
        self.max_radius = 40

    def eat(self):
        if self.radius < self.max_radius:
            self.radius += 2
        else:
            self.color = (200, 255, 255)

    def check_collision(self, other):
        dist = math.hypot(self.x - other.x, self.y - other.y)
        if dist < self.radius + other.radius:
            self.vel_x, other.vel_x = other.vel_x, self.vel_x
            self.vel_y, other.vel_y = other.vel_y, self.vel_y
            # Small push to prevent sticking
            self.x += self.vel_x
            self.y += self.vel_y