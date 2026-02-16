import pygame
import math 
from Vchito import Vchito
from Food import Food

# Pygame Initialization
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Vchitos Lab - Evolutionary Simulation")
clock = pygame.time.Clock()

# Simulation Population
vchitos_list = [Vchito() for _ in range(1)]
food_list = [Food()] 

# Timers
FOOD_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(FOOD_EVENT, 2000) # Spawns food every 2 seconds

running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                food_list.append(Food())
        
        if event.type == FOOD_EVENT:
            food_list.append(Food())

    # 2. Simulation Logic
    # 2.1 Update Food (Avoidance AI)
    for f in food_list:
        f.think(vchitos_list)
        f.move()

    # 2.2 Population Control
    new_vchitos_list = []
    for v in vchitos_list:
        # Check if Vchito is still alive (hunger check)
        if v.radius > 5.1:
            # Check for Mitosis (Success condition)
            if v.radius >= v.max_radius:
                # The parent splits and we add the children to the next frame
                new_vchitos_list.extend(v.split())
            else:
                # Normal behavior: hunt and move
                if food_list:
                    nearest_food = min(food_list, key=lambda f: math.hypot(v.x - f.x, v.y - f.y))
                    v.think(nearest_food)
                v.move()
                new_vchitos_list.append(v)
    
    vchitos_list = new_vchitos_list

    """
    vchitos_list = [v for v in vchitos_list if v.radius > 5.1]
    """


    
    # Ensure survival (Minimum population rules)
    if len(vchitos_list) == 0:
        vchitos_list.append(Vchito())
    if len(food_list) == 0:
        food_list.append(Food())

    # 2.3 Hunter Logic
    for v in vchitos_list:
        # Targeting
        if food_list:
            nearest_food = min(food_list, key=lambda f: math.hypot(v.x - f.x, v.y - f.y))
            v.think(nearest_food)
        
        v.move()
        
        # Collision Detection (Feeding)
        for f in food_list[:]:
            dist_to_food = math.hypot(v.x - f.x, v.y - f.y)
            if dist_to_food < v.radius + f.radius:
                v.eat()
                food_list.remove(f)

    # 2.4 Social Logic (Inter-vchito collisions)
    for i in range(len(vchitos_list)):
        for j in range(i + 1, len(vchitos_list)):
            vchitos_list[i].check_collision(vchitos_list[j])

    # 3. Rendering
    screen.fill((30, 30, 30)) # Dark background for better contrast
    
    for f in food_list:
        f.draw(screen)
    for v in vchitos_list:
        v.draw(screen)
    
    pygame.display.flip()
    clock.tick(60) # Locked at 60 FPS

pygame.quit()