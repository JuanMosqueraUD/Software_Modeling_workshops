# pip install black, black formater, pylint


class Engine:
    def __init__(
        self,
        torque: int,
        maximun_speed: int,
        dimensions: str,
        power: int,
        stability: str,
        weight: int,
    ):
        self.torque = torque
        self.maximun_speed = maximun_speed
        self.dimensions = dimensions
        self.power = power
        self.ststability = stability
        self.weight = weight


class GasEngine(Engine):

    pass


class ElectricEngine(Engine):
    pass
