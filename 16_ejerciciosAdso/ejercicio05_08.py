from utils import *
from datetime import datetime
"""
Ejercicio 05:
En este problema se ingresa un valor numérico de 8 dígitos que representa una fecha con elsiguiente formato: aaaammdd. Esto es: los 4 primeros dígitos
representan el año, los siguientes 2 dígitos representan el mes y los 2 dígitos  restantes representan el día. Se pide informar por separado el día, el mes y el año 
de la fecha ingresada. Para su solución se debe de hacer uso de divisiones, operador modulo y conversión de double a entero.

Ejercicio 8: ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente formato:
aaaammdd verificar si la fecha es correcta en sentido de numero de meses y días.
"""

def validar_fecha(cadena: str, formato: str = '%Y%m%d') -> bool:
    try:
        fecha = datetime.strptime(cadena, formato) #Convertir la cadena en un objeto datetime
        return True
    except ValueError as msg_error:
        return False

def extraer_fecha(fecha: int) -> ():  # Tupla
    # Sólucion conversión a String
    str_fecha = str(fecha)
    if len(str_fecha) == 8:
        if validar_fecha(str_fecha):
             # Desempaquetado de secuencias, segmentación de cadenas y tuplas
            return str_fecha[:4], str_fecha[4:6], str_fecha[6:]
        else:
            print(error(f"La cadena {str_fecha} no es una fecha real..."))
    else:
        print(error(f"La cadena {str_fecha} no esta en el formato correcto aaaammdd..."))

    return False

def menu_validar_fecha():
    """
    Método para validar si una fecha es valída en un formato de aaaammdd
    """
    print(info("Validar la fecha en formato (aaaammdd)"))

    numero = obtener_entero(info("Ingrese una fecha en el formato aaaammdd: "))
    result = extraer_fecha(numero)
    if result:
        print(confirm(f"La cadena '{numero}' representa la fecha {result[2]}/{result[1]}/{result[0]}, que es valida."))

if __name__ == '__main__':
    menu_validar_fecha()