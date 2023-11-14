from os import walk
import pygame

# os te da acceso a muchas funcionalidades del sistema

def importar_carpeta(path):
    superficie_lista = []
    # for informacion in walk(path):
    #     print(informacion)

    for _,__,archivos_imagenes in walk(path):
        for imagen in archivos_imagenes:
            path_completo = path + '/' + imagen
            imagen_surf = pygame.image.load(path_completo).convert_alpha()
            superficie_lista.append(imagen_surf)
    return superficie_lista