import csv
from typing import Any

from exceptions import FileError, NotDigitError


class Vehicle:
    vehicles: list = []

    def __init__(self, brand: str, model: str, number_wheels: int):
        self._brand = brand
        self._model = model
        self._number_wheels = self.validate_numeric(number_wheels, "El número de ruedas")

    def validate_numeric(self, value: Any, parameter_with_pronoun: str) -> int:
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
    def number_wheels(self, new_number_wheels: int) -> None:
        self._number_wheels = self.validate_numeric(new_number_wheels, "El número de ruedas")

    @classmethod
    def add_vehicle(cls, vehicle: Any) -> None:
        cls.vehicles.append(vehicle)

    @classmethod
    def save_data_csv(cls, name_file: str) -> None:
        try:
            with open(name_file, "w", encoding="utf-8", newline="") as file:
                file_csv = csv.writer(file)
                for item in cls.vehicles:
                    file_csv.writerow([item.__class__, item.__dict__])
        except Exception:
            raise FileError

    @staticmethod
    def read_data_csv(name_file: str) -> None:
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
        except Exception:
            raise FileError

        return vehicles

    def __str__(self) -> str:
        return f"Marca: {self.brand}, modelo: {self.model}, {self.number_wheels} ruedas"
