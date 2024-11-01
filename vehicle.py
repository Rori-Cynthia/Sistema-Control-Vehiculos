from exceptions import NotDigitError

class Vehicle:
    def __init__(self, brand: str, model: str, number_wheels):
        self._brand = brand
        self._model = model
        self._number_wheels = self.validate_numeric(number_wheels, "El número de ruedas")

    def validate_numeric(self, value, parameter_with_pronoun: str):
        if isinstance(value, int):
            return value
        elif isinstance(value, str) and value.isdigit():
            return int(value)
        else:
            raise NotDigitError(parameter_with_pronoun)
        
    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, new_brand: str) -> None:
        self._brand = new_brand

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, new_model: str) -> None:
        self._model = new_model

    @property
    def number_wheels(self) -> int:
        return self._number_wheels

    @number_wheels.setter
    def number_wheels(self, new_number_wheels) -> None:
        self._number_wheels = self.validate_numeric(new_number_wheels, "El número de ruedas")
