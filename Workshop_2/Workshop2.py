from abc import ABC



class Engine:  
    """This class represents the behaviour of a vehicle motor"""

    def __init__(
        self, stability: int, power: int, dimensions: int, weight: float, torque: int, maximun_speed:int, combustible_type:str
    ):
        self.stability=stability
        self.power= power
        self.dimensions= dimensions
        self.weight= weight
        self.torque= torque
        self.maximun_speed = maximun_speed
        self.combustible_type = combustible_type

    def __str__(self):
        return f"Name: {self.__name}    Type: {self.__type_}    \
            Potency: {self.__potency}    Weight: {self.__weight}"


class Low_engine_gama(Engine):

    def __innit__(self, gama):
        self.gama = gama

class Low_engine_gama(Engine):

    def __innit__(self, gama):
        self.gama = gama



class Vehicle:
    """This class is an abstraction of any vehicle"""

    def __init__(self, engine: Engine, chassis: str, model: str, year_car: int):
        self.engine = engine
        self.chasis = chassis
        self.model = model

class Car(Vehicle):
    """This class represents the behevior of a Car vehicle"""

    def __init__(self,vehicle: Vehicle, transmition: str, trade: str):
        self.vehicle = vehicle
        self.transmition=transmition
        self.trade=trade

 

class Truck(Vehicle):  
    """This class represents the behavior of a Truck vehicle"""

    def calculate_gas_consumption():
        return 0



class Yatch(Vehicle):
    """This class represents the behavior of a Yatch vehicle"""
    def __init__(self, vehicle: Vehicle, lenght: int, trade: str, weight: int):

        self.vehicle= vehicle
        self.lenght = lenght
        self.weight= weight
        self.trade=trade

class Motorcycle(Vehicle):
    """This class represents the behavior of a Motorcycle vehicle"""

class Helicopter(Vehicle):  
    """This class represents the behavior of a Helicopter vehicle"""

class Scooter(Vehicle):  
    """This class represents the behavior of a Scooter vehicle"""







MESSAGE = """
Option 1. Create engine
Option 2. Create car
Option 3. Create truck
Option 4. Create yatch
Option 5. Crear motorcyle
Option 6. create helicopter
Option 7. create scooter
Opcion 10. Exit
"""

engines = {}
vehicles = []


def create_engine():
    return 0


