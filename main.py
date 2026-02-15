import pygame
import math 
from vchito import Vchito
from food import Food

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Vchitos Lab - Collision System")
clock = pygame.time.Clock()

# Initialize entities
vchitos_list = [Vchito() for _ in range(8)] # Aumenté a 8 para ver más choques
pellet = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- LOGIC SECTION ---

    # 1. Individual updates (Movement & Food)
    for v in vchitos_list:
        v.move()
        
        # Distance to food
        dist_food = math.hypot(v.x - pellet.x, v.y - pellet.y)
        if dist_food < v.radius + pellet.radius:
            pellet.respawn()
            v.radius += 2 

    # 2. Group interaction (Vchito vs Vchito)
    # This is the part you were missing! 
    # We use a nested loop OUTSIDE the previous one for efficiency.
    for i in range(len(vchitos_list)):
        for j in range(i + 1, len(vchitos_list)):
            # Calling the method inside vchito.py
            vchitos_list[i].check_collision(vchitos_list[j])

    # --- RENDERING SECTION ---
    screen.fill((30, 30, 30))
    
    pellet.draw(screen)
    for v in vchitos_list:
        v.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()