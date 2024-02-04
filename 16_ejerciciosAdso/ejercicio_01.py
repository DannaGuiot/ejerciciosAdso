from utils import *

'''
    Ejercicio 01:
    En este problema, los datos de entrada son los dos valores enteros que ingresará el usuario a
    través del teclado (los llamaremos a y b) y la salida será su cociente (un número flotante). Ahora
    bien, existe la posibilidad de que el usuario ingrese como segundo valor el número 0 (cero). En
    este caso, no podremos mostrar el cociente ya que la división por cero es una indeterminación, así
    que tendremos que emitir un mensaje informando las causas por las cuales no se podrá efectuar
    la operación.
'''


def calcular_cociente(numero_1: int, numero_2: int) -> float:
    """
    Método que calcula el cociente
    :arg
    numero_1(int): Numerador.
    numero_2(int): Denominador.
     :return:
    - float: Cociente de la división.
    - str: Mensaje informativo si no se puede efectuar la operación.
    """

    if numero_2 == 0:
        print(error("La división es una indeterminación"))
        return 0
    else:
        return round(numero_1 / numero_2, 2)


def menu_cociente():
    '''
    Método para calcular el cociente de dos números enteros

    '''
    print(advertencia("Calculadora de cociente "))

    numero_1 = obtener_entero(info("Ingrese el primer número: "))
    numero_2 = obtener_entero(info("Ingrese el segundo número: "))

    resultado = calcular_cociente(numero_1, numero_2)
    if resultado:
        print(confirm(f"El resultado  del cociente es: {resultado}"))
    else:
        print(error(f"El denominador {resultado} no puede ser calculado"))


if __name__ == "_main_":
    menu_cociente()
