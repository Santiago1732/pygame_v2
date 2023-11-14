import sys
import pygame
from settings import *
from level import Level


pygame.init()
screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
clock = pygame.time.Clock()
level = Level(level_map,screen)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()
    # test_tile.draw(screen)

    pygame.display.update()
    clock.tick(60)