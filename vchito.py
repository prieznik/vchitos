import math
from Entity import Entity
from Brain import Brain
import random

class Vchito(Entity):
    """
    Main agent class.
    Handles metabolism, size-based speed, and social collisions.
    """
    def __init__(self, dna=None):
        # DNA logic
        if dna is None: 
            self.dna= {
                "speed_mult": random.uniform(0.5, 2.0),
                "metabolism_mult": random.uniform(0.5, 1.5)
            }
        else:
            self.dna = dna
        
        initial_speed = 1.0 * self.dna["speed_mult"]

        # Physic creation
        super().__init__(radius=15, color=(0, 255, 255), speed=initial_speed)
        self.max_radius = 40
        self.decay_rate = 0.003 * self.dna["metabolism_mult"] * self.dna["speed_mult"]

    def move(self):
        """Updates physics, metabolism, and state-based coloring."""
        # 1. Metabolism (Hunger)
        if self.radius > 5:
            self.radius -= self.decay_rate
        
        # 2. Dynamic State Color
        r = int(min(255, 0 + (self.dna["speed_mult"] * 50)))
        # White when at full capacity, Cyan otherwise
        if self.radius >= self.max_radius:
            self.color = (255, 255, 255)
        else:
            self.color = (r, 255, 255)
            
        # 3. Dynamic Speed Scaling (Inverse relation to size)
        base_radius = 15
        speed_factor = base_radius / self.radius
        speed_factor = max(0.4, min(speed_factor, 3.0)) 
        
        self.x += self.vel_x * speed_factor
        self.y += self.vel_y * speed_factor

        super().move()
        """
        # 4. Boundary bounce (inherited logic)
        if self.x <= self.radius or self.x >= 600 - self.radius:
            self.vel_x *= -1
        if self.y <= self.radius or self.y >= 400 - self.radius:
            self.vel_y *= -1
            """
    
    def think(self, target):
        """Adjusts velocity to track a target."""
        steer_x, steer_y = Brain.seek(self, target)
        self.vel_x += steer_x
        self.vel_y += steer_y

    def eat(self):
        """Increases mass on consumption."""
        if self.radius < self.max_radius:
            self.radius += 2

    def check_collision(self, other):
        """Elastic collision logic to prevent overlap and simulate impact."""
        dist = math.hypot(self.x - other.x, self.y - other.y)
        min_dist = self.radius + other.radius
        
        if dist < min_dist:
            dx = self.x - other.x
            dy = self.y - other.y
            if dist == 0: dist = 0.1
            
            # Repulsion impulse
            repulsion_power = 4.0
            self.vel_x = (dx / dist) * repulsion_power
            self.vel_y = (dy / dist) * repulsion_power
            other.vel_x = -(dx / dist) * repulsion_power
            other.vel_y = -(dy / dist) * repulsion_power
            
            # Position correction (Anti-sticking)
            overlap = min_dist - dist
            separation_boost = 1.5
            self.x += (dx / dist) * (overlap * separation_boost)
            self.y += (dy / dist) * (overlap * separation_boost)
            other.x -= (dx / dist) * (overlap * separation_boost)
            other.y -= (dy / dist) * (overlap * separation_boost)