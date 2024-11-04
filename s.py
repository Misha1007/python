import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))
WHITE = pygame.Color(255, 255, 255)
screen.fill(WHITE)

x=0
y=0
z=400
t=0
p=200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    y+=1
    if y>50:
        for i in range (250, 0, -1):
            y-=1
            pygame.draw.rect(screen, (255, 255, 255), (250, y, 50, 200))#прямоугольник Y
    x+=1
    if x>50:
        for j in range (250, 0, -1):
            x-=1
            pygame.draw.rect(screen, (255, 255, 255), (x, 300, 200, 50))#прямоугольник X
    z=-1
    if z>250:
        for l in range(400, 600, 1):
            for p in range(200, 250, 1):
                z+=1
            pygame.draw.rect(screen, (255, 255, 255), (300, z, 50, p))#прямоугольник Z
    t=-1
    if t>50:
        t=600
    pygame.draw.rect(screen, (255, 255, 0), (250, 250, 100, 100))#квадрат
    pygame.draw.rect(screen, (255, 0, 0), (250, y, 50, 200))#прямоугольник Y
    pygame.draw.rect(screen, (255, 0, 0), (x, 300, 200, 50))#прямоугольник X
    pygame.draw.rect(screen, (255, 0, 0), (300, z, 50, p))#прямоугольник Z
    pygame.draw.rect(screen, (255, 0, 255), (t, 250, 50, 200))#прямоугольник T
    pygame.display.update()

    pygame.time.delay(10)