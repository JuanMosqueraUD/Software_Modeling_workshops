from engines import Engine
from factories import EnginesFacade 

class Vehicle:
    """This class represents an abstraction of a vehicle inside the catalog business model."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
    ):
        self.engine = engine
        self.chassis = chassis
        self.price = price
        self.model = model
        self.year = year
        self.consumption = consumption

    def __str__(self):
        return f"Vehicle: {self.model} - {self.year} - {self.price} - \
            {self.consumption} - {self.engine} - {self.chassis}"


class Helicopter(Vehicle):
    """This class is a concrete implementation of an helicopter"""


class Scooter(Vehicle):
    """This class is a concrete implementation of a scoorter"""


class Motorcycle(Vehicle):
    """This class is a concrete implementation of a motorcycle"""


class Car(Vehicle):
    """This class is a concrete implementation of a car"""

    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
        transmission: str,
        trade: str,
        combustible_type: str,
    ):
        super().__init__(engine, chassis, price, model, year, consumption)
        self.transmission = transmission
        self.trade = trade
        self.combustible_type = combustible_type


class Truck(Vehicle):
    """This class is a concrete implemtantion of a truck"""

    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
    ):
        self.consumption = self.__calculate_gas_consupmtion()
        super().__init__(engine, chassis, price, model, year, self.consumption)


    def __calculate_gas_consupmtion(self) -> float:
        """
        This method calculates consumption based on engine
        values.

        Returns:
        - float: vehicle consumption
        """
        consumption = (
            (1.1 * self.engine.power)
            + (0.2 * self.engine.weight)
            + (0.3 if self.chassis == "A" else 0.5)
        )
        return consumption
    


class Yacht(Vehicle):
    """This class is a concrete implementation of a yatch"""

    def __init__(
        self,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
        length: float,
        weight: float,
        trade: str,
    ):
        super().__init__(engine, chassis, price, model, year, consumption)
        self.length = length
        self.weight = weight
        self.trade = trade

class EngineFlyweight:

    engines = {}
    
    @staticmethod
    def get_engine(self, type: str,price:str) -> Engine:

        if price == "low" and type == "electric":
            engine_type = "low-electric"
            if engine_type not in EngineFlyweight.engines:
                EngineFlyweight.engines[engine_type] =EnginesFacade.get_engine(type,price)
            else:
                return EngineFlyweight.engines[engine_type]
        elif price == "high" and type == "electric":
            engine_type = "high-electric"
            if engine_type not in EngineFlyweight.engines:
                EngineFlyweight.engines[engine_type] =EnginesFacade.get_engine(type,price)
            else:
                return EngineFlyweight.engines[engine_type]
        elif price == "low" and type == "gas":
            engine_type = "low-gas"
            if engine_type not in EngineFlyweight.engines:
                EngineFlyweight.engines[engine_type] =EnginesFacade.get_engine(type,price)
            else:
                return EngineFlyweight.engines[engine_type]
        elif price == "high" and type == "gas":
            engine_type = "high-gas"
            if engine_type not in EngineFlyweight.engines:
                EngineFlyweight.engines[engine_type] =EnginesFacade.get_engine(type,price)
            else:
                return EngineFlyweight.engines[engine_type]
        else:
            raise ValueError("Invalid engine type")