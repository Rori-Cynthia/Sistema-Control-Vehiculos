from bicycle import Bicycle
from car import Car
from cargo_car import CargoCar
from motorcycle import Motorcycle
from private_car import PrivateCar
from vehicle import Vehicle

classes_name = {
    "Vehicle": "Vehiculo",
    "Car": "Automovil",
    "PrivateCar": "Vehiculo Particular",
    "CargoCar": "Vehiculo de Carga",
    "Bicycle": "Bicicleta",
    "Motorcycle": "Motocicleta",
}


def create_car() -> None:
    cars = []

    try:
        number_cars_created = int(input("¿Cuantos vehículos desea insertar?: "))
    except ValueError:
        print("Ha ingresado un valor que no es un numero entero. Intentelo nuevamente")
        return create_car()

    if number_cars_created <= 0:
        print("Ha elegido no crear vehiculos.")
    else:
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
                return create_car()

        print("\nImprimiendo por pantalla los Vehiculos:\n")
        for number_car, car_data in enumerate(cars, start=1):
            print(f"Datos del automóvil {number_car}:", car_data)


def create_instances() -> None:
    private = PrivateCar("Ford", "Fiesta", 4, "180", "500", 5)
    cargo = CargoCar("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicycle = Bicycle("Shimano", "MT Ranger", 2, "Carrera")
    motorcycle = Motorcycle("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    instances_list = [private, cargo, bicycle, motorcycle]

    print("Nuevas instancias\n")
    for instance in instances_list:
        print(instance)

    print("\nRelación de instancia motocicleta con otras clases\n")
    for class_name in classes_name.keys():
        print(
            f"Motocicleta es instancia de {classes_name[class_name].capitalize()}: "
            f"{isinstance(motorcycle, globals()[class_name])}"
        )


def manage_data():
    """Data saving"""
    private = PrivateCar("Ford", "Fiesta", "4", "180", "500", "5")
    cargo = CargoCar("Daft Trucks", "G 38", "10", "120", "1000", "20000")
    bicycle = Bicycle("Shimano", "MT Ranger", 2, "Carrera")
    motorcycle = Motorcycle("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    instances_list = [private, cargo, bicycle, motorcycle]

    for instance in instances_list:
        Vehicle.add_vehicle(instance)

    Vehicle.save_data_csv("vehicles.csv")

    """Reading data"""
    vehicles_data = Vehicle.read_data_csv("vehicles.csv")

    classes_info = {class_name: [] for class_name in classes_name.keys()}

    for data in vehicles_data:
        data_class_name = data[0].split(".")[-1].rstrip("'>").lstrip("'")
        data_info = data[1]

        if data_class_name in classes_info:
            classes_info[data_class_name].append(data_info)

    for class_name, info_list in classes_info.items():
        if info_list:
            print(f"Lista de {classes_name[class_name]}:")
            for info in info_list:
                print(info)
            print()
