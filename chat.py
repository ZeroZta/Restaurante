"""
MODULO DE INTERFAZ PARA CHAT
Autor: ZeroZta
Versión: 1.0
Este módulo contiene las herramientas visuales 
para la terminal.
"""

# --- FUNCIONES ---

def borrar():
    """
    Limpia la terminal de comandos según 
    el sistema operativo.
    No requiere parámetros.
    """
    os.system('clear' if os.name == 'posix' else 'cls')

def mensaje(texto):
    """
    Imprime un texto encerrado entre dos
    líneas decorativas de 50 caracteres.
    Argumento:
    texto -- El String que se desea mostrar
    en pantalla.
    """
    print("="*50)
    print(texto)
    print("="*50)

def enter():
    """
    Pausa la ejecución del programa hasta
    que el usuario presione la tecla Enter.
    """
    input("\n Presiona Enter para avanzar...")

def ingresar(pregunta):
    """
    Muestra una pregunta al usuario y
    captura su respuesta desde el teclado.
    Retorna: La cadena de texto (string)
    ingresada por el usuario.
    """
    respuesta = input(f"\n {pregunta}")
    return respuesta

def barra(capacidad, puntos, divisor):
    """
    Calcula y despliega una barra de 
    progreso visual compuesta por '/' y '_'.
    
    Parámetros:
    capacidad -- Valor máximo de 
    referencia (int).
    puntos    -- Valor actual a representar 
    (int).
    divisor   -- Factor de escala para la 
    longitud de la barra (ej. 100).
    """
    # Lógica de cálculo
    porcentaje_total = int((puntos)/(capacidad/divisor))
    
    porcentaje_negativo = int((divisor - porcentaje_total)/(2))
    if porcentaje_negativo <= 0:
        porcentaje_negativo = 0
        
    porcentaje_positivo = int((porcentaje_total)/(2))
    
    diagonal = "/" * porcentaje_positivo
    barra_baja = "_" * porcentaje_negativo
    mensaje(f"{diagonal}{barra_baja}  {porcentaje_total}%")
