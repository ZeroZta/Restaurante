# Librerias:
import random
import chat
import Clientes
import pygame
import sys

# Funciones:

# Objetos:

# Instancias:
pygame.init()

# variables:
# Configuración de la ventana
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
# Colores (R, G, B)
BLANCO = (255, 255, 255)
ROSA = (255, 0, 93)
AZUL = (54,173, 154)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)
ROJO = (255, 0, 0)
VIOLETA = (128, 0, 128)
# Control de FPS (Fotogramas por segundo)
reloj = pygame.time.Clock()

# Inicio:
# Configuración de la ventana
pygame.display.set_caption("Mi primer juego - Sigue el mouse")

# Bucle Principal del Juego
while True:
    # --- Manejo de Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Si cierras la ventana
            pygame.quit()
            sys.exit()

    # --- Dibujo ---
    pantalla.fill(BLANCO)  # Limpiar la pantalla con un fondo blanco
    # Ubicación del mouse:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rect_x = mouse_x - 200
    rect_y = mouse_y - 150

    pygame.draw.rect(pantalla, ROSA, [rect_x, rect_y, 400, 300])
    pygame.draw.rect(pantalla, VERDE, [rect_x+100, rect_y + 75, 200, 150])
    pygame.draw.rect(pantalla, AMARILLO, [rect_x+150, rect_y + 112, 100, 75])
    pygame.display.flip()

    # Mantener el juego a 60 FPS
    reloj.tick(60)