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
    #forloop (100 es donde voy a iniciar en pixeles 700 a donde quiero ir y los ultimos 100 el numero de cada incremento 100 en 100)
    for x in range(100, 700, 100):
        pygame.draw.rect(screen, BLACK, (x, 50, 50, 50))
        pygame.draw.line(screen, GREEN, (x, 0,),(x, 100), 5)

    ####-----zona de dibujo
    #metodo para actualizar pantalla
    pygame.display.flip()



