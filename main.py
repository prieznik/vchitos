# main.py
import pygame
import math 
from Vchito import Vchito
from Food import Food

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Vchitos Lab - Inheritance System")
clock = pygame.time.Clock()

vchitos_list = [Vchito() for _ in range(8)]
pellet = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- LOGIC ---
    # 1. Update Food
    pellet.move()

    # 2. Population Control: Remove dead Vchitos (Radius <= 5)
    # This acts as the 'Natural Selection' filter
    vchitos_list = [v for v in vchitos_list if v.radius > 5.1]

    # 3. Individual Update Loop
    for v in vchitos_list:
        v.think(pellet) # AI calculation
        v.move()        # Physics + Metabolism
        
        # Check collision with Food
        dist_to_food = math.hypot(v.x - pellet.x, v.y - pellet.y)
        if dist_to_food < v.radius + pellet.radius:
            pellet.respawn()
            v.eat()

    # 4. Inter-population Interaction (Collisions)
    for i in range(len(vchitos_list)):
        for j in range(i + 1, len(vchitos_list)):
            vchitos_list[i].check_collision(vchitos_list[j])

    # --- RENDERING SECTION ---
    screen.fill((30, 30, 30))
    
    pellet.draw(screen)
    for v in vchitos_list:
        v.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()