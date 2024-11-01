from vehicle import Vehicle
from bicycle_motorcycle_enum import BicycleType
from exceptions import InvalidTypeBicycleError


class Bicycle(Vehicle):
    def __init__(self, brand: str, model: str, number_wheels: int, type_bicycle: BicycleType):
        super().__init__(brand, model, number_wheels)
        self._type_bicycle = self.validate_type_bicycle(type_bicycle)

    def validate_type_bicycle(self, type_bicycle):
        if type(self) is Bicycle and type_bicycle not in (BicycleType.URBAN, BicycleType.RACING):
            raise InvalidTypeBicycleError
        return type_bicycle

    @property
    def type_bicycle(self) -> BicycleType:
        return self._type_bicycle

    @type_bicycle.setter
    def type_bicycle(self, new_type_bicycle: BicycleType) -> None:
        self._type_bicycle = self.validate_type_bicicle(new_type_bicycle)

    def __str__(self) -> str:
        return (
            f"Marca: {self.brand}, modelo: {self.model}, "
            f"{self.number_wheels} ruedas, tipo: {self.type_bicycle}"
        )
