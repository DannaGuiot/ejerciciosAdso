from utils import *
import math

"""
Ejercicio 3: En este problema debemos de definir una constante con el valor de PI como 3,1416 y tenemos un único dato de entrada dado por el usuario:
un valor numérico que puede ser entero o flotante que indicara el radio de un círculo. La salida del algoritmo será el área del circulo teniendo en cuenta
que A=PI*r^2. Si el usuario ingresó valor negativo o cero tendremos que emitir un mensaje informando las causas por las cuales no se podrá efectuar la operación.
"""

def calcular_area(numero: int | float) -> bool | float:
    """
        Método que calcula el area de un círculo
        :arg
        numero(int|float): Número que hace referencia a la medida del circulo.

         :return:
        -  bool|float: Area del círculo.
        - str: Mensaje informativo si no se puede efectuar la operación.
        """

    if numero <= 0:
        print(error("ERROR: El número debe ser mayor a cero"))
        return False
    else:
     return round(math.pi * math.pow(numero, 2), 2)


def menu_radio_circulo():
    """
    Método para calcular el radio de un circulo.
    """
    print(confirm("Calculadora de area de un círculo "))
    numero = obtener_flotante(info("Ingrese el valor del radio del círculo: "))
    result = calcular_area(numero)
    if result:
        print(confirm(f"Para un circulo de {numero} de radio es: {result}"))
    else:
        print(error(f"Para un circulo de {numero} no se puede calcular el area"))

if __name__ == "__main__":
  menu_radio_circulo()


