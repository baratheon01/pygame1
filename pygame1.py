import pygame, sys
pygame.init()

#Definir colores
BLACK   =(  0,  0,  0)
WHITE   =(255, 255, 255)
GREEN   =(0, 255, 0)
RED     =(255,  0,  0)
BLUE    =(0,  0,  255)

#width y height
size = (800, 500)

#crear ventana
screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    #metodo para poner color de fondo
    screen.fill(WHITE)
    ####----zona de dibujo
    pygame.draw.line(screen, GREEN, [0, 100], [200, 300], 5)
    pygame.draw.rect(screen, BLACK, (100, 100, 80,80))
    pygame.draw.circle(screen, BLACK, (200,200), 30)

    ####-----zona de dibujo
    #metodo para actualizar pantalla
    pygame.display.flip()



