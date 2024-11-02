from bicycle_motorcycle_enum import BicycleType

class NotDigitError(Exception):
    def __init__(self, parameter_name):
        self.parameter_name = parameter_name
        self.message = (f"{self.parameter_name} debe ser un número entero positivo "
                        f"o una cadena de texto que represente un número entero positivo.")
        super().__init__(self.message)

class InvalidTypeBicycleError(Exception):
    def __init__(self):
        self.mensaje = (
            f"Las bicicletas solo pueden ser de tipo {BicycleType.URBAN} o de "
            f"{BicycleType.RACING}."
        )
        super().__init__(self.mensaje)

class FileError(Exception):
    def __init__(self, mensaje="Error al cargar o guardar el inventario."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)