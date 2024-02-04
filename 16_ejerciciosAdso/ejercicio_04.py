from utils import *

"""
Ejercicio 4: En este problema tenemos un único dato de entrada: un valor numérico entero que deberá ingresar el usuario.
La salida del algoritmo será informar si el numero ingresado  por el usuario es múltiplo de 2 y 3. Sabemos que un número es
múltiplo de otro cuando al dividir estos dos números el residuo sea 0. Si el usuario ingresó un valor negativo o cero tendremos que emitir
un mensaje informando las causas por las cuales no se podrá efectuar la operación.
"""


def calcular_multiplo(numero: int) -> bool:
    """
        Método que calcula si un número es múltiplo de 2 y 3.
        :arg
        numer(int): Número a validar.
        :return: - bool: Validar si es múltiplo o no de 2 y 3.
        - str: Mensaje informativo si no se puede efectuar la operación.

    """
    if numero <= 0:
        print(error("El número debe ser mayor a cero"))
        return False
    return numero % 2 == 0 and numero % 3 == 0


def menu_multiplo():
    """
        Método para calcular si es múltiplo de 2 y 3
    """
    print(advertencia("Validar si es número ingresado es múltiplo de 2 y 3"))

    numero = obtener_entero(info("Ingrese el número: "))
    resultado = calcular_multiplo(numero)
    print(f"El número: {numero} {resultado and confirm('SI') or error('NO')} es un múltiplo de 2 y 3")


if __name__ == "__main__":
    menu_multiplo()
