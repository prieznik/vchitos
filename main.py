import pygame
import math # Needed for square root
from vchito import Vchito
from food import Food

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Initialize entities
vchitos_list = [Vchito() for _ in range(5)]
pellet = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logic
    for v in vchitos_list:
        v.move()
        
        # COLLISION DETECTION: Calculate distance to food
        # Distance = sqrt( (x2-x1)^2 + (y2-y1)^2 )
        dist = math.hypot(v.x - pellet.x, v.y - pellet.y)
        
        # If distance is less than the sum of their radii, it's a collision!
        if dist < v.radius + pellet.radius:
            pellet.respawn()
            v.radius += 2 # Vchito grows when it eats!

    # Rendering
    screen.fill((30, 30, 30))
    pellet.draw(screen)
    for v in vchitos_list:
        v.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()