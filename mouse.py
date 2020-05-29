import pygame, sys
pygame.init()

black = (0, 0, 0)
white =(255, 255, 255)
red = (255, 0, 0)
size =(800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
#se establece visibilidad de mouse siendo 0 false y 1 true
pygame.mouse.set_visible(0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #a traves de pygame podemos traer la posicion del mouse sobre toda nuestra  pantalla de juego
    #ponemos este metodo en una variable para luego usarla como constante de nuestro eje x, y
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    screen.fill(white)

    pygame.draw.rect(screen, red, (x, y, 100, 100))

    pygame.display.flip()
clock.trick(60)
