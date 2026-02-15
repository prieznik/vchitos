import math
import random
from Entity import Entity
from Brain import Brain

class Food(Entity):
    """
    Resource class.
    Includes avoidance logic to escape from Vchitos.
    """
    def __init__(self):
        super().__init__(radius=5, color=(0, 255, 0), speed=1.0)
        self.max_escape_speed = 2.0 

    def think(self, hunter_list):
        """Analyzes surroundings and escapes from nearby hunters."""
        if not hunter_list:
            return

        total_steer_x = 0
        total_steer_y = 0
        danger_count = 0

        # Perception: Evaluate all Vchitos in range
        for v in hunter_list:
            dist = math.hypot(self.x - v.x, self.y - v.y)
            if dist < 120:
                steer_x, steer_y = Brain.flee(self, v)
                # Influence weight based on distance
                weight = (120 - dist) / 120
                total_steer_x += steer_x * weight
                total_steer_y += steer_y * weight
                danger_count += 1

        if danger_count > 0:
            # Apply cumulative escape force
            self.vel_x += total_steer_x * 0.8
            self.vel_y += total_steer_y * 0.8
            
            # Dynamic speed clamping
            current_speed = math.hypot(self.vel_x, self.vel_y)
            if current_speed > self.max_escape_speed:
                ratio = self.max_escape_speed / current_speed
                self.vel_x *= ratio
                self.vel_y *= ratio
        else:
            # Natural drift when safe
            current_speed = math.hypot(self.vel_x, self.vel_y)
            if current_speed < 1.0:
                self.vel_x += (random.random() - 0.5) * 0.2
                self.vel_y += (random.random() - 0.5) * 0.2
            
            if current_speed > 1.0:
                self.vel_x *= 0.99
                self.vel_y *= 0.99

    def respawn(self):
        """Randomly teleports the entity across the screen."""
        self.x = random.randint(20, 580)
        self.y = random.randint(20, 380)