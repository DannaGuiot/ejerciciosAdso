from utils import *

"""
Ejercicio 2
En este problema tenemos un único dato de entrada: un valor numérico entero que deberá ingresar el usuario. La salida del algoritmo será
informar si el usuario ingresó un valor par o impar. Sabemos que un número par es aquel que es divisible por 2 o, también,
que un número es par si el valor residual que se obtiene al dividirlo por 2 es cero. Según lo anterior, podremos informar que el número
ingresado por el usuario es par si al dividirlo por 2 obtenemos un resto igual a cero. De lo contrario, informaremos que el número es impar.
"""


def numero_es_par(numero: int) -> bool:
    """
    Método que calcula si un número es par o no.
          :arg
    numero(int): Numero ingresado.

     :return:
    - Bool: Valida si es par o no.
    - str: Mensaje informativo si no se puede efectuar la operación.
    """
    return numero % 2 == 0


def menu_par():
    '''
        Método para calcular si un número es par o no.
    '''

    print(advertencia("Validar número par o impar"))

    numero = obtener_entero(info("Ingrese el número a validar: "))

    print(confirm("El número es: " + ("par" if numero_es_par(numero) else "impar")))


if __name__ == "__main__":
    menu_par()
