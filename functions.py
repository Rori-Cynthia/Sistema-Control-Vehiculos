from bicycle import Bicycle
from car import Car
from cargo_car import CargoCar
from motorcycle import Motorcycle
from private_car import PrivateCar
from vehicle import Vehicle


def create_car() -> None:
    cars = []
    number_cars_created = int(input("¿Cuantos vehículos desea insertar?: "))

    for car in range(1, number_cars_created + 1):
        try:
            print(f"\nDatos del automovil {car}")
            input_brand = input("Inserte la marca del automovil: ")
            input_model = input("Inserte el modelo del automovil: ")
            input_number_wheels = int(input("Inserte el número de ruedas: "))
            input_speed = int(input("Inserte velocidad en Km/h: "))
            input_displacement = int(input("Inserte el cilindraje en cc: "))

            new_car = Car(
                input_brand,
                input_model,
                input_number_wheels,
                input_speed,
                input_displacement,
            )
            cars.append(new_car)
        except ValueError:
            print("Uno de los datos ingresados es invalido. Por favor, reingrese los datos")

    print("\nImprimiendo por pantalla los Vehiculos:\n")
    for number_car, car_data in enumerate(cars, start=1):
        print(f"Datos del automóvil {number_car}:", car_data)


def create_vehicles() -> None:
    print("Nuevas instancias\n")
    private = PrivateCar("Ford", "Fiesta", 4, "180", "500", 5)
    cargo = CargoCar("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicycle = Bicycle("Shimano", "MT Ranger", 2, "Carrera")
    motorcycle = Motorcycle("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehicles = [private, cargo, bicycle, motorcycle]

    for vehicle in vehicles:
        print(vehicle)

    print("\nRelación de instancia motocicleta con otras clases\n")
    print(f"Motocicleta es instancia de Vehiculo: {isinstance(motorcycle, Vehicle)}")
    print(f"Motocicleta es instancia de Automovil: {isinstance(motorcycle, Car)}")
    print(
        f"Motocicleta es instancia de Vehículo PaOrticular: {isinstance(motorcycle, PrivateCar)}"
    )
    print(f"Motocicleta es instancia de Vehículo de Carga: {isinstance(motorcycle, CargoCar)}")
    print(f"Motocicleta es instancia de Bicicleta: {isinstance(motorcycle, Bicycle)}")
    print(f"Motocicleta es instancia de Motocicleta: {isinstance(motorcycle, Motorcycle)}")
