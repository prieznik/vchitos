import pygame

class Wall:
    """
    Static environmental obstacle.
    Defines physical boundaries that entities cannot cross.
    """
    def __init__(self, x, y, w, h):
        # Using pygame.Rect for easy collision detection
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (100, 100, 100) # Neutral gray for infrastructure

    def draw(self, surface):
        """Renders the wall on the provided surface."""
        pygame.draw.rect(surface, self.color, self.rect)