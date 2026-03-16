# Librerias:
import random
import chat


# Funciones:
def barra_decorada(capacidad, puntos):
    """
    Muestra visualmente una barra de progreso decorada en la consola.

    Args:
        capacidad (int/float): El valor total que representa el 100% de la barra.
        puntos (int/float): El progreso actual a representar.
    """
    print(chat.mensaje(chat.barra(capacidad, puntos)))

# Objetos:
class Cliente:
    """
    Representa a un cliente con niveles de hambre y tiempo de espera aleatorios.

    Attributes:
        hambre (int): La cantidad de puntos necesaria para que el cliente esté satisfecho.
        tiempo_de_espera (int): El tiempo máximo que el cliente está dispuesto a esperar.
        puntos_actuales (int): La cantidad de puntos consumidos hasta el momento.
        satisfecho (bool): Estado que indica si el cliente ha comido lo suficiente.
    """

    def __init__(self):
        """Inicializa un nuevo cliente con atributos aleatorios."""
        self.hambre = random.randint(30, 150)
        self.tiempo_de_espera = random.randint(15, 60)
        self.puntos_actuales = 0
        self.satisfecho = False

    def comer(self):
        """
        Simula el acto de comer seleccionando un platillo al azar.
        Suma el valor del platillo a los puntos actuales del cliente.
        """
        platillos = [30, 35, 40, 45, 50]
        puntos_comida = random.choice(platillos)
        self.puntos_actuales += puntos_comida

    def estado(self):
        """
        Verifica y actualiza si el cliente ha alcanzado su nivel de satisfacción.

        Returns:
            bool: True si los puntos actuales igualan o superan el hambre, False de lo contrario.
        """
        if self.puntos_actuales >= self.hambre:
            self.satisfecho = True
        return self.satisfecho

# Inicio: