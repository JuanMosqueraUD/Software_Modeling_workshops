from engines import Engine

# import engine because it is the interface for the other engines


class Vehicle:

    def __init__(
        self,
        engine: Engine,
        chasis,
        price: int,
        model: str,
        year: int,
        consumption: float,
    ):
        self.engine = engine		
        self.chasis = chasis
        self.price = price
        self.model = model
        self.year = year
        self.consumption = consumption
        
class Car (Vehicle):
    def __init__(self, engine: Engine, chasis, price: int, model: str, year: int, consumption: float,transmission, trade, combustible_type):
        super().__init__(engine, chasis, price, model, year, consumption)
    	self.transmission = transmission
        self.trade = trade
        self.combustible_type = combustible_type

class Truck(Vehicle):
    def __init__(self, engine: Engine, chasis, price: int, model: str, year: int, consumption: float) -> None:
		super().__init__(engine, chasis, price, model, year, consumption)

	def calculate_gas_comsuption():
         pass

def yatch(Vehicle):
	pass


