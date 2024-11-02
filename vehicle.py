from exceptions import NotDigitError, FileError
import csv

class Vehicle:
    vehicles = []

    def __init__(self, brand: str, model: str, number_wheels):
        self._brand = brand
        self._model = model
        self._number_wheels = self.validate_numeric(number_wheels, "El número de ruedas")

    def validate_numeric(self, value, parameter_with_pronoun: str):
        if isinstance(value, int):
            if value < 0:
                raise NotDigitError(parameter_with_pronoun)
            return value
        elif isinstance(value, str) and value.isdigit():
            value = int(value)
            if value < 0:
                raise NotDigitError(parameter_with_pronoun)
            return value
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

    @classmethod
    def add_vehicle(cls, vehicle):
        cls.vehicles.append(vehicle)

    @classmethod
    def save_data_csv(cls, name_file):
        try:
            with open(name_file, "w", encoding="utf-8", newline="") as file:
                file_csv = csv.writer(file)
                for item in cls.vehicles:
                    file_csv.writerow([item.__class__, item.__dict__])
        except:
            raise FileError

    @staticmethod
    def read_data_csv(name_file):
        vehicles = []
        try:
            with open(name_file, "r", encoding="utf-8") as file:
                file_csv = csv.reader(file)
                for vehicle in file_csv:
                    vehicles.append(vehicle)
            if not vehicles:
                print(f"El archivo '{name_file}' está vacío.")
        except FileNotFoundError:
            print(f"El archivo '{name_file}' no se encontró. Se creará uno nuevo.")
            with open(name_file, "w", encoding="utf-8") as file:
                pass
        except:
            raise FileError

        return vehicles

    def __str__(self) -> str:
        return (
            f"Marca: {self.brand}, modelo: {self.model}, {self.number_wheels} ruedas")