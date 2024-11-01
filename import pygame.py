import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))
WHITE = pygame.Color(255, 255, 255)
screen.fill(WHITE)

BLACK = pygame.Color(0, 0, 0)
BLUE = pygame.Color(0, 255, 255)
YELLOW = pygame.Color(255, 255, 0)
BROWN = pygame.Color(57,22, 2)
MAROON = pygame.Color(128, 0, 0)

pygame.draw.rect(screen, YELLOW, (225, 225, 150, 150))

pygame.draw.polygon(screen, BROWN, ([225,225], [375, 225], [300, 113]))

pygame.draw.circle(screen, BLUE, (270, 300), 30)
pygame.draw.line(screen, BLACK, (270, 270), (270, 330))
pygame.draw.line(screen, BLACK, (240, 300), (300, 300))

pygame.draw.rect(screen, MAROON, ([310, 300, 55, 75]))
pygame.draw.circle(screen, YELLOW, (360, 323), 4)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    pygame.display.update()