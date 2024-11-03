from bicycle import Bicycle
from bicycle_motorcycle_enum import BicycleType, EngineType, FrameType, validate_enum


class Motorcycle(Bicycle):
    def __init__(
        self,
        brand: str,
        model: str,
        number_wheels: int,
        type_motorcycle: BicycleType,
        type_engine: EngineType,
        type_frame: FrameType,
        spoke_numbers: int,
    ):
        super().__init__(brand, model, number_wheels, type_motorcycle)
        self._type_engine = validate_enum(type_engine, EngineType, "tipo de motor")
        self._type_frame = validate_enum(type_frame, FrameType, "tipo de cuadro")
        self._spoke_numbers = self.validate_numeric(spoke_numbers, "El número de radios")

    @property
    def spoke_numbers(self) -> int:
        return self._spoke_numbers

    @spoke_numbers.setter
    def spoke_numbers(self, new_spoke_numbers: int) -> None:
        self._spoke_numbers = self.validate_numeric(new_spoke_numbers, "El número de radios")

    @property
    def type_frame(self) -> FrameType:
        return self._type_frame

    @type_frame.setter
    def type_frame(self, new_type_frame: FrameType) -> None:
        self._type_frame = validate_enum(new_type_frame, FrameType, "tipo de cuadro")

    @property
    def type_engine(self) -> EngineType:
        return self._type_engine

    @type_engine.setter
    def type_engine(self, new_type_engine: EngineType) -> None:
        self._type_engine = validate_enum(new_type_engine, EngineType, "tipo de motor")

    def __str__(self) -> str:
        return (
            f"Marca: {self.brand}, modelo: {self.model}, "
            f"{self.number_wheels} ruedas, tipo: {self.type_bicycle}, "
            f"motor: {self.type_engine}, cuadro: {self.type_frame}, "
            f"Nro radios: {self.spoke_numbers}"
        )
