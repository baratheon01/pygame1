import pygame, sys, random
pygame.init()

white= (255, 255, 255)
red = (255, 0, 0)

size = (800, 500)
screen = pygame.display.set_mode(size)
#se establece una reloj que va a dar la velocidad de fps
clock = pygame.time.Clock()
#se establece una lista para ocuparla con las coordenadas x, y que parten desde 0 hasta sus rangos maximos
coor_list =[]
#el range de 60 es el numero de puntos con los que se va a llenar el espacio
for i in range(60):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        coor_list.append([x, y])

while True:
    #en este for establecemos el even mediante el import de sys para que pueda cerrar el juego con la pestaña x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(white)
    #en este for se dibuja el circulo, dandole color, medidas y diametro
    for j in coor_list:
        x = j[0]
        y = j[1]
        pygame.draw.circle(screen, red, (x, y ), 2)
        #se incrementa el y y se le da un condicional para que el ciclo se repita entre 1 y 0 
        j[1] +=1
        if j[1] > 500:
            j[1] = 0
    pygame.display.flip()
    clock.tick(30)