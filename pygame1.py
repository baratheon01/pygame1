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

#controlar FPS
clock = pygame.time.Clock()

#coordenadas
cord_x = 400
cord_y = 200

#velocidad a la que se movera mi cuadrado
speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    if(cord_x > 720 or cord_x < 0):
        speed_x *= -1
    if(cord_y > 400 or cord_y < 0):
        speed_y *= -1
    cord_x += speed_x
    cord_y += speed_y
    #metodo para poner color de fondo
    screen.fill(WHITE)
    ####----zona de dibujo
    #forloop (100 es donde voy a iniciar en pixeles 700 a donde quiero ir y los ultimos 100 el numero de cada incremento 100 en 100)
    #pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))

    ####-----zona de dibujo
    #metodo para actualizar pantalla
    pygame.display.flip()
    clock.tick(60)



