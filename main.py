import pygame

# 1. Inicializar
pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Mi primer Vchito")

# 2. Variables del bicho
pos_x, pos_y = 300, 200
color_bicho = (0, 255, 255) # Un celeste neón

# 3. Loop del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Dibujar fondo y bicho
    ventana.fill((30, 30, 30)) # Gris oscuro
    pygame.draw.circle(ventana, color_bicho, (pos_x, pos_y), 20)
    
    pygame.display.flip()

pygame.quit()
