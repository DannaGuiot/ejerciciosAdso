from utils import *

"""
Ejercicio 12: Se debe de ingresar un numero por el usuario, este debe de ser evaluado para verificar que el
número de cifras sea par y verificar si el número es capicúa o no.
"""

def obtener_numero_positivo() -> str:
    """
           Función para validar solo números enteros.
            """
    while True:
        try:
            numero = obtener_entero(info("Ingrese un número: "))
            if numero > 0:
                return numero
            else:
                print(error("Error: Ingrese un número entero positivo."))
        except ValueError:
            print(error("Error: Ingrese un número entero válido."))


def es_capicua(numero: int) -> bool:
    """
    Método que verifica si el número es par de cifras y si es capicúa.
    :arg
    número(int): Número a operar.
    return:
    bool: Dermita si es falso o verdadero sobre el número.
    - str: Mensaje informativo si no se puede efectuar la operación.
    """

    numero_str = str(numero)  # Convierte el número a cadena para facilitar la manipulación de dígitos

    if len(numero_str) % 2 != 0:  # Verifica si el número de dígitos es par
        return False

    for i in range(len(numero_str) // 2):  # Compara los dígitos de la izquierda con los de la derecha
        if numero_str[i] != numero_str[-(i + 1)]:
            return False

    return True


def menu_cap():
    """
            Función para verificar si un número es par de cifras y capicúa o no.
     """

    numero = obtener_numero_positivo()
    if es_capicua(numero):
        print(confirm(f"El número {numero} es capicúa con un número par de dígitos."))
    else:
        print(error(f"El {numero} no es un número capicúa o no tiene un número par de dígitos."))


if __name__ != "__main__":
    pass
else:
    menu_cap()
