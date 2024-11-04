import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))
WHITE = pygame.Color(255, 255, 255)
screen.fill(WHITE)

x=0
y=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    y+=1
    if y>600:
        y=0
    x+=1
    if x>600:
        x=0
    pygame.draw.rect(screen, (255, 255, 0), (250, 250, 100, 100))
    pygame.draw.rect(screen, (255, 0, 0), (250, y, 50, 200))
    pygame.draw.rect(screen, (255, 0, 0), (x, 250, 200, 50))
    pygame.draw.rect(screen, (255, 0, 255), (x, 250, 200, 50))
    pygame.draw.rect(screen, (255, 0, 255), (250, y, 50, 200))
    pygame.display.update()

    pygame.time.delay(10)