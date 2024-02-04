def texto_color(texto: str, color: str = "blanco", decoration: int = 0) -> str:
    """
        Método para darle color al texto
        :arg
        texto (str): Texto al que se le va dar color.
        color (str): Color que se le va a asignar al texto.
    """

    ascii_color = "\033[39m {}\033[00m"
    if color == "negro":
        color = "\033[30m {}\033[00m"
    elif color == "rojo_oscuro":
        color = "\033[31m {}\033[00m"
    elif color == "verde_oscuro":
        color = "\033[32m {}\033[00m"
    elif color == "amarillo_oscuro":
        color = "\033[33m {}\033[00m"
    elif color == "azul_oscuro":
        color = "\033[34m {}\033[00m"
    elif color == "magenta_oscuro":
        color = "\033[35m {}\033[00m"
    elif color == "cyan_oscuro":
        color = "\033[36m {}\033[00m"
    elif color == "gris":
        color = "\033[37m {}\033[00m"
    elif color == "gris_oscuro":
        color = "\033[90m {}\033[00m"
    elif color == "rojo":
        color = "\033[91m {}\033[00m"
    elif color == "verde":
        color = "\033[92m {}\033[00m"
    elif color == "amarillo":
        color = "\033[93m {}\033[00m"
    elif color == "azul":
        color = "\033[94m {}\033[00m"
    elif color == "magenta":
        color = "\033[95m {}\033[00m"
    elif color == "cyan":
        color = "\033[96m {}\033[00m"
    elif color == "blanco":
        color = "\033[97m {}\033[00m"
    return color.format(texto)


def info(texto: str) -> str:
    """
        Método para generar un mensaje de ihformación.

        :arg
        texto: Texto del mensaje de ihformación.

        :return:
        texto: Texto en formato de ihformación.
         """
    return texto_color(texto, "azul")


def error(texto: str) -> str:
    """
     Método para generar un mensaje error

     :arg
     texto: Texto del mensaje de error.

     :return:
     texto: Texto en formato de error.
      """
    return texto_color(texto, "rojo")


def advertencia(texto: str) -> str:
    """
        Método para generar un mensaje de advertencia.

        :arg
        texto: Texto del mensaje de advertencia.

        :return:
        texto: Texto en formato de error.
    """
    return texto_color(texto, "amarillo")


def confirm(texto: str) -> str:
    """
    Método para generar un mensaje de confirmación.

     :arg
     texto: Texto del mensaje de confirmación .

     :return:
      texto: Texto en formato de confirmación.
    """
    return texto_color(texto, "verde")


def obtener_entero(mensaje: str = None) -> int:
    """
               Método para validar y solicitar un número entero.

               :arg
                mensaje:  texto para solocitar el número.
               :return:
                valor: número entero.
       """
    valor = input(mensaje if mensaje is not None else info("Ingrese un número entero: "))
    while True:
        try:
            return int(valor)
        except ValueError:
            print(error(f"El texto {valor} no se puede convertir a número"))
            valor = input(advertencia("Ingresa nuevamente un número entero: "))


def obtener_flotante(mensaje: str = None) -> float:
    """
               Método para validar y solicitar un número flotante.

               :arg
                mensaje:  texto para solocitar el número.
               :return:
                valor: número flotante.
       """
    valor = input(mensaje if mensaje is not None else info("Ingrese un número flotante: "))
    while True:
        try:
            return float(valor)
        except ValueError:
            print(error(f"El texto {valor} no se puede convertir a número"))
            valor = input(advertencia("Ingresa nuevamente un número flotante: "))



        if __name__ == '__main__':
            pass
