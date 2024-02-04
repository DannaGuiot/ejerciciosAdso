from utils import *

"""
Ejercicio 16: Desarrollar un algoritmo que solicite una frase de mínimo 5 palabras y capitalizar la cadena.
"""


def capitalizar_frase(frase: str) -> str:
    """
    Método que capitaliza una cadena.
    :arg
    frase(str): Cadena a calcular.
    return:
    str: Devolver cadena capitalizada.
    str: Mensaje informativo si no se puede efectuar la operación.
    """

    palabras = frase.split()
    if len(palabras) < 5:
        return "La frase debe tener al menos 5 palabras."

    frase_capitalizada = frase.title()# Capitalizar la primera letra de cada palabra en la frase
    return frase_capitalizada


def menu_capitalizar():
    """
        Función capitaliza una cadena.
    """

    frase = input(info("Ingrese una frase de al menos 5 palabras: "))
    resultado = capitalizar_frase(frase)
    print(confirm(f"La frase capitalizada es: {resultado}"))


if __name__ == "__main__":
    menu_capitalizar()
