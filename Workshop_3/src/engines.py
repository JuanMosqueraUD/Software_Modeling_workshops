class Engine:
    """This class represents an abstraction of an engine for any vehicle."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        torque: int,
        maximum_speed: int,
        dimenssions: str,
        power: int,
        stability: str,
        weight: float,
        combustion_type: str,
    ):
        self.torque = torque
        self.maximum_speed = maximum_speed
        self.dimenssions = dimenssions
        self.power = power
        self.stability = stability
        self.weight = weight
        self.combustion_type = combustion_type


class EngineType:
    """This class represents an abstraction of an engine type for any vehicle."""

    def __init__(self, engine_type: str):
        self.engine_type = engine_type
        self.engine= create_engine(engine_type) # type: ignore

    def create_engine(self, engine_type: str) -> Engine:
        """This method creates an engine based on the engine type."""
        if engine_type == "electric-highend":
            return ElectricEngine("highend")
        elif engine_type == "gasoline-highend":
            return GasEngine("highend")
        elif engine_type == "electric-lowend":
            return ElectricEngine("lowend")
        elif engine_type == "gasoline-lowend":
            return GasEngine("lowend")
        else:
            raise ValueError("Invalid engine type")


class EngineFactory:
    """This class is an abstract factory to create both gas and electric engines."""

    EngineTypes = {}

    @staticmethod
    def get_engine_type(engine_type: str) -> Engine:
        """This method returns an engine based on the engine type."""
        if engine_type not in EngineFactory.EngineTypes:
            EngineFactory.EngineTypes[engine_type] = EngineType(engine_type).engine
        return EngineFactory.EngineTypes[engine_type]


class ElectricEngine(Engine):
    """This class represents an abstraction of an electric engine for any vehicle."""

    def __init__(self, gama: str):
        self.gama = gama

        if gama == "highend":
            self.create_highend()
            super().__init__(
                self.torque,
                self.maximum_speed,
                self.dimenssions,
                self.power,
                self.stability,
                self.weight,
                self.combustion_type,
            )
        if gama == "lowend":
            self.create_lowend()
            super().__init__(
                self.torque,
                self.maximum_speed,
                self.dimenssions,
                self.power,
                self.stability,
                self.weight,
                self.combustion_type,
            )

    def create_highend(self):
        """
        Creates a high-end engine with specific attributes.
        """
        self.torque = 180
        self.maximum_speed = 300
        self.dimensions = "200x200x200"
        self.power = 200
        self.stability = "high"
        self.weight = 100.9
        self.combustion_type = "electric"

    def create_lowend(self):

        self.torque = 90
        self.maximum_speed = 100
        self.dimenssions = "100x100x100"
        self.power = 100
        self.stability = "low"
        self.weight = 50.9
        self.combustion_type = "electric"

class GasEngine(Engine):
    """This class represents an abstraction of a gas engine for any vehicle."""

    def __init__(self, gama: str):
        self.gama = gama

        if gama == "highend":
            self.create_highend()
            super().__init__(
                self.torque,
                self.maximum_speed,
                self.dimenssions,
                self.power,
                self.stability,
                self.weight,
                self.combustion_type,
            )
        if gama == "lowend":
            self.create_lowend()
            super().__init__(
                self.torque,
                self.maximum_speed,
                self.dimenssions,
                self.power,
                self.stability,
                self.weight,
                self.combustion_type,
            )

    def create_highend(self):
        """this method creates a high-end engine with specific attributes."""
        self.torque = 210
        self.maximum_speed = 400
        self.dimenssions = "210x200x250"
        self.power = 250
        self.stability = "medium"
        self.weight = 120.5
        self.combustion_type = "gasoline"
    
    def create_lowend(self):
        """this method creates a low-end engine with specific attributes."""
        self.torque = 110
        self.maximum_speed = 200
        self.dimenssions = "110x100x150"
        self.power = 150
        self.stability = "low"
        self.weight = 70.5
        self.combustion_type = "gasoline"
    