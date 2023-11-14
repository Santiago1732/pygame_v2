import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,posicion,tamanio):
        super().__init__()
        self.image = pygame.Surface((tamanio,tamanio))
        self.image.fill("grey")
        self.rect = self.image.get_rect(topleft = posicion)

    def update(self, x_shift):
        self.rect.x += x_shift
