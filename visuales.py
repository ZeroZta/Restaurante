
# - Libreria:
# ===============
import sys
import pygame
import random
import chat
import Clientes
# ===============

# - Instancia:
# ===============
pygame.init()
# ===============

# - Variables
# ===============
# Pantalla:
ancho, largo = 800, 600
pantalla = pygame.display.set_mode((ancho, largo))
reloj = pygame.time.Clock()

# Circulo:
radio = 50
radio2 = 100
centrado_x = ancho // 2
centrado_y = largo // 2
centradoXY = (centrado_x, centrado_y)
centradoXY2 = (centrado_x, centrado_y)
# Mouse:
flecha = [(1, 1), (5, 35), (10, 22), (33, 43), (42, 34), (21, 10), (35, 5)]
# Colores:
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
blanco = (255, 255, 255)
negro = (0,0,0)
magenta = (255, 0, 255)
amarillo = (255, 239, 55)
# ===============

# - Funciones:
# ===============
# ===============

# - Objetos
# ===============
# ===============

# - Inicio:
# ===============
# Configuración de la ventana
pygame.display.set_caption("Mi primer juego - Sigue el mouse")
while True:
    # 1. Gestion de Eventos:
    # Salir:
    for evento in pygame.event.get():        
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        """
        if evento.type == pygame.MOUSEBUTTONDOWN:
             centradoXY = evento.pos
        """

    # 2. Logica:
        #Mouse logica:
    px,py = pygame.mouse.get_pos()
    flecha_transformada = []
    for posicion in flecha:
        mx = (posicion[0]*2)+(px)
        my = (posicion[1]*2) + (py)
        flecha_transformada.append((mx,my))
    

    # 3. Dibujo:
        # Fondo:
    pantalla.fill(blanco)
    
        # Frente:
            # Mouse:
    pygame.draw.polygon(pantalla,amarillo,flecha_transformada,0)
    pygame.draw.polygon(pantalla,negro,flecha_transformada,5)
    # 4. Actualizacion de pantalla:
    pygame.display.update()
    reloj.tick(60)

# ===============
