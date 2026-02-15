# vchito.py
import math
from Entity import Entity
from Brain import Brain

class Vchito(Entity):
    def __init__(self):
        # Inherit from Entity: radius 15, cyan, speed 1.0 (or whatever you prefer)
        super().__init__(radius=15, color=(0, 255, 255), speed=1.0)
        self.max_radius = 40
        self.decay_rate = 0.003  # How much radius is lost per frame

    def move(self):
        """
        Updates position with a dynamic speed scaling.
        Small Vchitos get a significant boost to hunt efficiently.
        """
        # 1. Energy Decay (Hunger)
        if self.radius > 5:
            self.radius -= self.decay_rate
            
        # 2. DYNAMIC SPEED SCALING
        # Base radius is 15. 
        # If radius = 7.5 (small), speed_factor = 2.0 (Double speed!)
        # If radius = 30 (large), speed_factor = 0.5 (Half speed)
        base_radius = 15
        speed_factor = base_radius / self.radius
        
        # We can "clamp" the factor so they don't go at light speed 
        # or stop moving entirely.
        speed_factor = max(0.4, min(speed_factor, 3.0)) 
        
        # 3. Apply displacement using the factor
        self.x += self.vel_x * speed_factor
        self.y += self.vel_y * speed_factor

        # 4. Boundary bounce logic
        if self.x <= self.radius or self.x >= 600 - self.radius:
            self.vel_x *= -1
        if self.y <= self.radius or self.y >= 400 - self.radius:
            self.vel_y *= -1
    
    def think(self, target):
        """Uses the brain to adjust velocity WITHOUT resetting the object."""
        steer_x, steer_y = Brain.seek(self, target)
        
        self.vel_x += steer_x
        self.vel_y += steer_y

    def eat(self):
        if self.radius < self.max_radius:
            self.radius += 2
        else:
            self.color = (200, 255, 255)

    def check_collision(self, other):
        dist = math.hypot(self.x - other.x, self.y - other.y)
        min_dist = self.radius + other.radius
        
        # We check for a slight overlap to trigger the "explosion"
        if dist < min_dist:
            # 1. CALCULATE DIRECTION
            dx = self.x - other.x
            dy = self.y - other.y
            if dist == 0: dist = 0.1 # Prevent division by zero
            
            # 2. REPULSION FORCE (The "Explosion" component)
            # Instead of just swapping, we assign new velocities 
            # pointing AWAY from each other with high magnitude.
            repulsion_power = 4.0 # Boost this number to increase dispersion
            
            self.vel_x = (dx / dist) * repulsion_power
            self.vel_y = (dy / dist) * repulsion_power
            other.vel_x = -(dx / dist) * repulsion_power
            other.vel_y = -(dy / dist) * repulsion_power
            
            # 3. POSITION CORRECTION (Anti-sticking)
            # Move them far apart immediately so they don't collide again next frame
            overlap = min_dist - dist
            separation_boost = 1.5 # Extra push factor
            
            self.x += (dx / dist) * (overlap * separation_boost)
            self.y += (dy / dist) * (overlap * separation_boost)
            other.x -= (dx / dist) * (overlap * separation_boost)
            other.y -= (dy / dist) * (overlap * separation_boost)