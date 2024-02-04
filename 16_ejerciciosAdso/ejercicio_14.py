from utils import *

"""
Ejercicio 14: Desarrollar un algoritmo que determine si una cadena de caracteres es palíndroma. Una
cadena se dice palíndromo si al invertirla es igual a ella misma.
"""


def es_palindromo(cadena: str) -> bool:
    """
        Método que calcula que determina si una cadena de caracteres es palíndroma.
        :arg
        cadena (str): Cadena a calcular.
        caracter (str): Caracter a contar.
        return:
        bool: Si es verdadero o falso.
        str: Mensaje informativo si no se puede efectuar la operación.
    """

    cadena_procesada = ''.join(
        c.lower() for c in cadena if c.isalnum())  # Convierte la cadena a minúsculas y elimina los espacios en blanco
    return cadena_procesada == cadena_procesada[::-1]  # Compara la cadena original con su versión invertida


def menu_palindromo():
    """
           Función para determinar si una cadena de caracteres es palíndroma.
    """

    cadena = input(info("Ingrese una cadena de caracteres: "))
    if es_palindromo(cadena):
        print(confirm(f"La cadena {cadena} es un palíndromo."))
    else:
        print(error(f"La cadena {cadena} no es un palíndromo."))


if __name__ == "__main__":
    menu_palindromo()
