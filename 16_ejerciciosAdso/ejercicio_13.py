from utils import *

"""
Ejercicio 13: Desarrollar un algoritmo que reciba como entrada un carácter y de cómo salida el número de
ocurrencias de dicho carácter en una cadena de caracteres.
"""


def contar_ocurrencias(cadena: str, caracter: str) -> int:
    """
    Método que calcula el número  de ocurrencias de un carácter de una cadena de caracteres.
    :arg
    cadena (str): Cadena a calcular.
    caracter (str): Caracter a contar.
     str: Mensaje informativo si no se puede efectuar la operación.
        """

    return cadena.count(caracter)


def menu_cadena():
    """
           Función para alcular el número  de ocurrencias de un carácter de una cadena de caracteres.
    """

    cadena = input(info("Ingrese una cadena de caracteres: "))
    caracter_a_contar = input(info("Ingrese el carácter que desea contar: "))

    ocurrencias = contar_ocurrencias(cadena, caracter_a_contar)
    print(confirm(f"El carácter '{caracter_a_contar}' aparece {ocurrencias} veces en la cadena."))


if __name__ == "__main__":
    menu_cadena()
