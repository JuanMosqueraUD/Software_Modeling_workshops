class Engine:  
    """This class represents the behaviour of a vehicle motor"""

    def __init__(
        self, stability: int, power: int, dimensions: int, weight: float, torque: int, maximun_speed:int
    ):
        self.stability=stability
        self.power= power
        self.dimensions= dimensions
        self.weight= weight
        self.torque= torque
        self.maximun_speed = maximun_speed

    def __str__(self):
        return f"Name: {self.__name}    Type: {self.__type_}    \
            Potency: {self.__potency}    Weight: {self.__weight}"


class Vehicle:
    """This class is an abstraction of any vehicle"""

    def __init__(self, engine: Engine, chassis: str, model: str, year_car: int):
        self.__engine = engine
        self.__chasis = chassis
        self.__model = model
        self.__year = year_car
        self.__consumption = self.__calculate_gas_consupmtion()
