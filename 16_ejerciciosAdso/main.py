import ejercicio_01
import ejercicio_02
import ejercicio_03
import ejercicio_04
import ejercicio05_08
import ejercicio_06
import ejercicio_07
import ejercicio_09
import ejercicio_10
import ejercicio_11
import ejercicio_12
import ejercicio_13
import ejercicio_14
import ejercicio_15
import ejercicio_16
from utils import *

def menu():
    while True:
        print(" ")
        print(confirm("-----Menú principal-----"))
        print(advertencia("1) Cociente de 2 números."))
        print(advertencia("2) Verificar número par o impar."))
        print(advertencia("3) Hallar Radio del círculo."))
        print(advertencia("4) Verificar si es múltiplo de 2 y 3."))
        print(advertencia("5) Validar si una fecha es correcta."))
        print(advertencia("6) Ordenar números de mayor a menor."))
        print(advertencia("7) Calcular la hipotenusa de un triángulo."))
        print(advertencia("9) Mostrar un mes a partir de un número."))
        print(advertencia("10) Convertir segundos a Horas, minutos y segundos restantes."))
        print(advertencia("11) Mostrar números inversamente."))
        print(advertencia("12) Verificar si un número es par de cifras y capicua."))
        print(advertencia("13) Contar número de ocurrencias de un carácter en una cadena."))
        print(advertencia("14) Determinar si una cadena de caracteres es palíndroma."))
        print(advertencia("15) Pedir un número de 0 a 99 y mostrarlo escrito."))
        print(advertencia("16) Capitalizar la cadena."))
        print(error("0) Salir"), end="\n", sep="-")
        print(confirm("Seleccione un ejercicio a ejecutar: "))

        opcion = obtener_entero("")
        if opcion == 1:
            ejercicio_01.menu_cociente()
        elif opcion == 2:
            ejercicio_02.menu_par()
        elif opcion == 3:
            ejercicio_03.menu_radio_circulo()
        elif opcion == 4:
            ejercicio_04.menu_multiplo()
        elif opcion == 5:
            ejercicio05_08.menu_validar_fecha()
        elif opcion == 6:
            ejercicio_06.menu_extremos()
        elif opcion == 7:
            ejercicio_07.menu_hipotenusa()
        elif opcion == 9:
            ejercicio_09.obtener_numero_mes()
        elif opcion == 10:
            ejercicio_10.menu_convertir_seg()
        elif opcion == 11:
            ejercicio_11.mennu_numero()
        elif opcion == 12:
            ejercicio_12.menu_cap()
        elif opcion == 13:
            ejercicio_13.menu_cadena()
        elif opcion == 14:
            ejercicio_14.menu_palindromo()
        elif opcion == 15:
            ejercicio_15.menu_palabras()
        elif opcion == 16:
            ejercicio_16.menu_capitalizar()
        elif opcion == 0:
            print(info("Programa finalizado..."))
            exit(0)
        else:
            print(error("Opción no valida..."))


if __name__ == '__main__':
    print(info("Bienvenido al desarrollo del taller de lógica de programación con python"))
    print(info("Nombres: Danna Nikool Guiot Daza"))
    print(info("Ficha: 2670142"), end="\n")
    menu()
