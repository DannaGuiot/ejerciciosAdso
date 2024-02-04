from utils import *
from num2words import num2words

"""
Ejercicio 15: Pedir un número de 0 a 99 y mostrarlo escrito. Por ejemplo, para 56 mostrar: cincuenta y seis.
"""


def numero_a_palabras(numero: int) -> str:
    """
        Método que convierte un número a su versión escrita.
        :arg
        cadena (str): Cadena a calcular.
        número(int): Número a convertir.
        str: Número escrito.
        str: Mensaje informativo si no se puede efectuar la operación.
    """

    if 0 <= numero <= 99:
        numero_palabras = num2words(numero, lang='es')  # Convertir el número en palabras en español

        return numero_palabras
    else:
        return "Número fuera de rango. Ingresa un número entre 0 y 99."


def menu_palabras():
    """
    Función para conviertir un número a su versión escrita.
    """

    numero = obtener_entero(info("Ingrese un número entre 0 y 99: "))
    resultado = numero_a_palabras(numero)
    print(confirm(f"El número {numero} en palabras es: {resultado}"))



if __name__ == "__main__":
    menu_palabras()
