from utils import *

""" 
Ejercicio 10:
Dado un número (leído por teclado), que representa los segundos que ha invertido una 
persona en hacer un examen, determinar cuántas horas, minutos y segundos ha invertido. 
Imprima el resultado por pantalla. 
"""

def obtener_entero_positivo():
    while True:
        try:
            valor = float(input(info("Ingrese la cantidad de segundos que ha invertido en hacer un examen: ")))
            if valor > 0:
                return valor
            else:
                print(error("Por favor, ingrese un número entero positivo."))
        except ValueError:
            print(error("Por favor, ingrese un número entero válido."))

def convertir_segs(segundos: float):
    """
            Método que convierte segundos a tiempo.
            :arg
            segundos(int): Número a operar.
            - str: Mensaje informativo si no se puede efectuar la operación.
    """
    hours = int(segundos // 3600)
    minutes = int(segundos % 3600 // 60)
    seconds = int(segundos % 60)
    return f"Invirtio {hours} horas, {minutes} minutos, {seconds} segundos, realizando el examen."


def menu_convertir_seg():
    """
        Función para convertir segundos a tiempo horas, minutos y segundos.
    """
    seconds = obtener_entero_positivo()
    print(confirm(convertir_segs(seconds)))


if __name__ == "__main__":
    menu_convertir_seg()
