from car import Car


class PrivateCar(Car):
    def __init__(
        self,
        brand: str,
        model: str,
        number_wheels: int,
        speed: int,
        displacement: int,
        number_seats: int,
    ):
        super().__init__(brand, model, number_wheels, speed, displacement)
        self._number_seats = self.validate_numeric(number_seats, "El número de asientos")

    @property
    def number_seats(self) -> int:
        return self._number_seats

    @number_seats.setter
    def number_seats(self, new_number_seats: int) -> None:
        self._number_seats = self.validate_numeric(new_number_seats, "El número de asientos")

    def __str__(self) -> str:
        return (
            f"Marca: {self.brand}, modelo: {self.model}, "
            f"{self.number_wheels} ruedas, {self.speed} km/h, "
            f"{self.displacement} cc, puestos: {self.number_seats}"
        )
