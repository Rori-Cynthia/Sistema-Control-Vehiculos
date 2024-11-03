from car import Car


class CargoCar(Car):
    def __init__(
        self,
        brand: str,
        model: str,
        number_wheels: int,
        speed: int,
        displacement: int,
        load_weight: int,
    ):
        super().__init__(brand, model, number_wheels, speed, displacement)
        self._load_weight = self.validate_numeric(load_weight, "El peso de la carga")

    @property
    def load_weight(self) -> int:
        return self._load_weight

    @load_weight.setter
    def load_weight(self, new_load_weight: int) -> None:
        self._load_weight = self.validate_numeric(new_load_weight, "El peso de la carga")

    def __str__(self) -> str:
        return (
            f"Marca: {self.brand}, modelo: {self.model}, "
            f"{self.number_wheels} ruedas, {self.speed} km/h, "
            f"{self.displacement} cc, {self.load_weight} kg"
        )
