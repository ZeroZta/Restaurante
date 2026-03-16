# Librerias:
import random
import chat

# Funciones:
def barra_decorada(capacidad, puntos):
    """
    Esta funcion sirve para decorar la barra de progreso:

    Args:
        capacidad: Necesita un valor que represente el 100% de la barra.
        puntos: Es el valor actual que se desea representar en la barra.
    """
    
    print(chat.mensaje(chat.barra(capacidad, puntos)))
# Objetos:
class Cliente:
    # Funcion Inicial:
    def __init__ (self):
        self.hambre = random.randint(30,150)
        self.tiempo_de_espera= random.randint(15,60)
        self.puntos_actuales = 0
        self.satisfecho = False
    # Funcion para comer:    
    def comer(self):
        platillos = [30,35,40,45,50]
        self.puntos = random.choice(platillos)
        self.puntos_actuales += self.puntos
    # Estado del cliente: 
    def estado(self):
         if self.puntos_actuales >= self.hambre:
             self.satisfecho = True
         return self.satisfecho
# Inicio:
