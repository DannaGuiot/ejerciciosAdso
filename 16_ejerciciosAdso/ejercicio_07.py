from utils import *

"""
Ejercicio 07: Calcular la hipotenusa de un triángulo, teniendo como base el valor del cateto 1 y 2 que serán  dados por el usuario. Para esto debe 
de hacer uso del Teorema de Pitágoras en el cálculo de la hipotenusa teniendo los catetos. (h= √(a^2 )+b^2) no se debe hacer uso de la librería Math.hypot
"""

def obtener_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print(error("Por favor, ingrese un número positivo."))
        except ValueError:
            print(error("Por favor, ingrese un número válido."))

def calcular_hipotenusa(cate_1: float, cate_2: float) -> float:
    """
     Método que calcula que la hipotenusa de un triángulo.
     :arg
     cate_1, cate_2, (int): Número a calcular.
     :return:
     - float: Número float
     - str: Mensaje informativo si no se puede efectuar la operación.
    """
    hipotenusa = (((cate_1 ** 2) + (cate_2 ** 2)) ** 0.5)
    return round((hipotenusa), 2)


def menu_hipotenusa():
    """
    Función para calcular la hipotenusa de un triángulo.
     """
    print(advertencia("Hallar la hipotenusa de un triágulo"))
    cate1 = obtener_numero_positivo(info("Ingrese la longitud del primer cateto: "))
    cate2 = obtener_numero_positivo(info("Ingrese la longitud del segundo cateto: "))

    hipotenusa = calcular_hipotenusa(cate1, cate2)
    print(confirm(f"La hipotenusa del triángulo es: {hipotenusa}"))

if __name__ == "__main__":
    menu_hipotenusa()
