from utils import *

"""
Ejercicio 06:
Leer tres valores numéricos enteros, indicar cuál es el mayor, cuál es el del medio y cuál, el
menor. Considerar que los tres valores serán diferentes.
"""


def obtener_entero_positivo():
    while True:
        try:
            valor = int(input(info("Ingrese un número entero positivo: ")))
            if valor > 0:
                return valor
            else:
                print(error("Por favor, ingrese un número entero positivo."))
        except ValueError:
            print(error("Por favor, ingrese un número entero válido."))


def numeros_extremos(num_1: int, num_2: int, num_3: int) -> ():
    """
           Método que calcula que número es el mayor, medio y menor.
           :arg
           num_1, num_2,num_3(int): Número a identificar.
            :return:
           - (): Devolver tupla mayor, medio y menor.
           - str: Mensaje informativo si no se puede efectuar la operación.
    """

    menor, medio, mayor = sorted([num_1, num_2, num_3])
    return mayor, medio, menor


def menu_extremos():
    """
        Método para calcular el número mayor, del medio y menor.
    """

    while True:
        print(advertencia("Identificar que número es el mayor, el del medio y el menor"))

        num_1 = obtener_entero_positivo()
        num_2 = obtener_entero_positivo()
        num_3 = obtener_entero_positivo()

        if num_1 == num_2 or num_2 == num_3 or num_1 == num_3:

            print(error("Error: Los valores deben ser diferentes, inténtelo nuevamente."))
        else:
            mayor, medio, menor = numeros_extremos(num_1, num_2, num_3)
            print(confirm(f"Número mayor: {mayor}, Numero del medio: {medio}, Número menor: {menor}"))

if __name__ == "__main__":
    menu_extremos()
