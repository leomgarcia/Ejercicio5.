# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

# Ejercicio 3: Cambiar el tamaño de página.
size = [1300, 600]
ancho = int(input("Ancho de la pantalla: "))
alto = int(input("Alto de la pantalla: "))
size[0] = ancho
size[1] = alto

# Ejercicio de Clase 4: Cambiar título de la pestaña.
titulo = input("Título del juego: ")

# Ejercicio 4: Cambiar color del fondo.
colorR = int(input("Rojo: "))
colorG = int(input("Verde: "))
colorB = int(input("Azul: "))
fondo = (colorR, colorG, colorB)
main2(size, titulo, fondo)