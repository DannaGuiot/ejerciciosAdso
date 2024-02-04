import calendar
import locale
from utils import *

"""
Ejercicio 9: Se debe de ingresar un numero comprendido entre 1 y 12 por el usuario. El algoritmo debe 
de imprimir el mes correspondiente en texto. 
"""


def obtener_numero_mes():
    """
         Método que muestra un mes a partir de un número entre el 1 y 12"
         :arg
         numero_mes (int): Número a verificar si corresponde a un mes, entre el 1 y 12.
         :return:
         - str: Mes obtenido.
         - str: Mensaje informativo si no se puede efectuar la operación.
    """

    while True:
        try:
            numero_mes = obtener_entero(info("Ingrese un número entre 1 y 12: "))
            if 1 <= numero_mes <= 12:
                return numero_mes
            else:
                print(error("Error: El número debe estar en el rango de 1 a 12. Inténtelo nuevamente."))
        except ValueError:
            print(error("Error: Ingrese un número entero válido."))


def imprimir_mes(numero_mes: int) -> str:
    """
        Función para calcular un mes a partir de un número.
         """
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')# Establecer la localización en español
    nombre_mes = calendar.month_name[numero_mes]# Obtener el nombre del mes en español

    print(confirm(f"El número {numero_mes} corresponde al mes de {nombre_mes}."))

def main():
    numero_mes = obtener_numero_mes()
    imprimir_mes(numero_mes)


if __name__ == "__main__":
    main()
