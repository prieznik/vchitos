# food.py
from Entity import Entity
import random

class Food(Entity):
    def __init__(self):
        # Inherit from Entity: radius 5, green, speed 1.5
        super().__init__(radius=5, color=(0, 255, 0), speed=1.5)

    def respawn(self):
        """Specific food behavior: teleport to random spot."""
        # We reuse the logic but could also just re-init position
        self.x = random.randint(20, 580)
        self.y = random.randint(20, 380)