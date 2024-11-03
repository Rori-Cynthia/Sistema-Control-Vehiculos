from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand: str, model: str, number_wheels: int, speed: int, displacement: int):
        super().__init__(brand, model, number_wheels)
        self._speed = self.validate_numeric(speed, "La velocidad")
        self._displacement = self.validate_numeric(displacement, "La cilindrada")

    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    def speed(self, new_speed: int) -> None:
        self._speed = self.validate_numeric(new_speed, "La velocidad")

    @property
    def displacement(self) -> int:
        return self._displacement

    @displacement.setter
    def displacement(self, new_displacement: int) -> None:
        self._displacement = self.validate_numeric(new_displacement, "La cilindrada")

    def __str__(self) -> str:
        return (
            f"Marca: {self.brand}, modelo: {self.model}, "
            f"{self.number_wheels} ruedas, {self.speed} km/h, "
            f"{self.displacement} cc"
        )
