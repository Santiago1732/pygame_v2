import pygame
from soporte import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.importar_imagenes()
        self.imagen_index = 0
        self.velocidad_animacion = 0.15
        self.image = self.animaciones['corriendo'][self.imagen_index]
        self.rect = self.image.get_rect(topleft = pos)

        # movimiento player
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 20
        self.gravity = 2
        self.jump_speed = -16

        self.cara_derecha = True
    #


    def importar_imagenes(self):
        imagenes_path = 'imagenes/character/'
        self.animaciones  = {'inactivo':[], 'saltando':[], 'corriendo':[],'cayendo':[]}

        for animacion in self.animaciones.keys():
            path_completo = imagenes_path + animacion
            self.animaciones[animacion] = importar_carpeta(path_completo)


    def animar(self):
        animacion = self.animaciones[self.estado]

        # loop por cada index
        self.imagen_index += self.velocidad_animacion
        if self.imagen_index >= len(animacion):
            self.imagen_index = 0

        imagen = animacion[int(self.imagen_index)]
        if self.cara_derecha:
            # CHEQUEAR
            self.image = imagen
        else:
            flipped_image = pygame.transform.flip(imagen,True,False)
            self.image = flipped_image


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 0.8
            # DIRECCION DE LA CARA
            self.cara_derecha = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -0.8
            # DIRECCION DE LA CARA
            self.cara_derecha = False
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.jump()

    # {'inactivo': [], 'saltando': [], 'corriendo': [], 'cayendo': []}
    def obtener_estado(self):
        if self.direction.y < 0:
            self.estado = 'saltando'
        elif self.direction.y > 0:
            self.estado = 'cayendo'
        elif self.direction.x > 0 or self.direction.x < 0:
            self.estado = 'corriendo'
        else:
            self.estado = 'inactivo'


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed


    def update(self):
        self.get_input()
        self.obtener_estado()
        self.animar()
