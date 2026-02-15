# brain.py
import math

class Brain:
    """
    Steering Behavior Logic.
    Calculates forces to move entities towards targets.
    """
    @staticmethod
    def seek(actor, target):
        """
        Calculates the steering force towards a target.
        actor: The entity that wants to move (Vchito)
        target: The goal entity (Food)
        """
        # 1. Vector from Actor to Target
        dx = target.x - actor.x
        dy = target.y - actor.y
        distance = math.hypot(dx, dy)

        if distance > 0:
            # 2. Desired Velocity (The perfect path at max speed)
            desired_x = (dx / distance) * actor.speed
            desired_y = (dy / distance) * actor.speed

            # 3. Steering Force: (Desired - Current Velocity) * smoothing_factor
            # We use 0.05 to make the turn smooth, not instant.
            steer_x = (desired_x - actor.vel_x) * 0.05
            steer_y = (desired_y - actor.vel_y) * 0.05
            
            return steer_x, steer_y
        
        return 0, 0