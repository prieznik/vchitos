# src/Poison.py
import random
from Entity import Entity

class Poison(Entity):
    def __init__(self):
        # Give it a small speed so it drifts
        super().__init__(radius=6, color=(255, 0, 0), speed=1.5)