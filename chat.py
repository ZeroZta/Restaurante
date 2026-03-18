"""
Módulo de Interfaz para Chat.
Proporciona utilidades visuales y de interacción para la terminal.

Autor: ZeroZta
Versión: 1.3
"""

import os

# --- FUNCIONES ---

def borrar():
    """Limpia la consola según el sistema operativo."""
    os.system('clear' if os.name == 'posix' else 'cls')

def mensaje(texto):
    """
    Devuelve un bloque de texto decorado con líneas horizontales.
    Args:
        texto (str): El contenido a mostrar.
    Returns:
        str: Texto con separadores de 50 caracteres.
    """
    contorno = "=" * 50
    return f"{contorno}\n{texto}\n{contorno}"

def enter():
    """Pausa la ejecución hasta que se presiona Enter."""
    input("\n Presiona Enter para avanzar...")

def ingresar(pregunta):
    """
    Solicita una entrada al usuario.
    Args:
        pregunta (str): Instrucción para el usuario.
    Returns:
        str: Respuesta del usuario.
    """
    return input(f"\n {pregunta}")

def barra(capacidad, puntos):
    """
    Genera una barra de progreso visual de 50 caracteres de largo.

    Args:
        capacidad (int/float): El valor que representa el 100%.
        puntos (int/float): El valor actual.

    Returns:
        str: Representación visual con '/' para lleno, '_' para vacío y el %.
        None: Si la capacidad es 0.
    """
    try:
        porcentaje_total = int((puntos * 100) / capacidad)
    except ZeroDivisionError:
        print("Error: La capacidad debe ser mayor a cero.")
        return None

    # Ajuste para que la barra visual no se desborde (0 a 100)
    llenado_limite = max(0, min(porcentaje_total, 100))

    # Dibujo de la barra (cada carácter representa 2%)
    positivo = int(llenado_limite / 2)
    negativo = int((100 - llenado_limite) / 2)

    return f"{'/' * positivo}{'_' * negativo}  {porcentaje_total}%"