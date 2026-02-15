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
        self.base_radius = 15
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
        speed_factor = self.base_radius / self.radius
        speed_factor = max(0.4, min(speed_factor, 3.0)) 
        
        self.x += self.vel_x * speed_factor
        self.y += self.vel_y * speed_factor

        super().move()
    
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

    def split(self):
        """
        Creates two children with inherited DNA and a small mutation.
        Returns a list of two new Vchitos.
        """
        children = []
        for _ in range(2):
            # Apply a small mutation (e.g., +/- 10%)
            child_dna = {
                "speed_mult": self.dna["speed_mult"] * random.uniform(0.9, 1.1),
                "metabolism_mult": self.dna["metabolism_mult"] * random.uniform(0.9, 1.1)
            }
            
            # Clamp DNA values to keep them within realistic bounds
            child_dna["speed_mult"] = max(0.5, min(child_dna["speed_mult"], 3.0))
            child_dna["metabolism_mult"] = max(0.5, min(child_dna["metabolism_mult"], 2.0))
            
            # Spawn child at parent's location
            child = Vchito(dna=child_dna)
            child.x, child.y = self.x, self.y
            child.radius = self.base_radius # Children start at base size
            children.append(child)
            
        return children