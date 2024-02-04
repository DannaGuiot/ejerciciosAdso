from utils import *

"""
Ejercicio 11: Dado un número entero leído por pantalla, muestre cada uno de los dígitos del número en
orden inverso. Ej: Si el número es 324, se debe mostrar 4, 2, 3.
"""


def obtener_numero_positivo() -> str:
    """
           Función para validar solo números enteros.
            """
    while True:
        try:
            numero = obtener_entero(info("Ingrese una cadena de número enteros: "))
            if numero > 0:
                return numero
            else:
                print(error("Error: Ingrese un número entero positivo."))
        except ValueError:
            print(error("Error: Ingrese un número entero válido."))


def obtener_digitos_inversos_cadena(numero: int) -> str:
    """
              Método que convierte numeros a orden inverso.
              :arg
              número(int): Número a invertir.
              -str: Cadena de números invertidos.
              - str: Mensaje informativo si no se puede efectuar la operación.
      """
    digitos = [digito for digito in str(numero)]
    digitos_inversos = ''.join(reversed(digitos))
    return digitos_inversos


def mennu_numero():
    numero = obtener_numero_positivo()
    digitos_inversos = obtener_digitos_inversos_cadena(numero)

    print(confirm("Dígitos en orden inverso:"), digitos_inversos)


if __name__ == "__main__":
    mennu_numero()
