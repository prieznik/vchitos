import math

class Brain:
    """
    Utility class for Steering Behaviors.
    Provides static methods to calculate movement forces.
    """
    @staticmethod
    def seek(actor, target):
        """Calculates force to move towards a target."""
        dx = target.x - actor.x
        dy = target.y - actor.y
        distance = math.hypot(dx, dy)
        
        if distance > 0:
            # Desired velocity at max speed
            desired_x = (dx / distance) * actor.speed
            desired_y = (dy / distance) * actor.speed
            
            # Steering = (Desired - Current Velocity) * Smoothing Factor
            steer_x = (desired_x - actor.vel_x) * 0.05
            steer_y = (desired_y - actor.vel_y) * 0.05
            return steer_x, steer_y
        return 0, 0

    @staticmethod
    def flee(actor, danger):
        """Calculates force to move away from a danger source."""
        seek_x, seek_y = Brain.seek(actor, danger)
        return -seek_x, -seek_y