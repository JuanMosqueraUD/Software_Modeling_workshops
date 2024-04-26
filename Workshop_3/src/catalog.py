from typing import List

from vehicles import Vehicle

class Catalog:

    def __init__(self):
        self.__vehicles = List[Vehicle]

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Catalog, cls).__new__(cls)
            cls.instance.vehicles = []
        return cls.instance

    def get_all_vehicles(self) -> List[Vehicle]:
        return self.__vehicles

    def get_price_by_range(self, min_price: float, max_price: float) -> List[Vehicle]:
        return [vehicle for vehicle in self.__vehicles if min_price <= vehicle.price <= max_price]
    
    def search_max_speed(self, max_speed: int) -> List[Vehicle]:
        return [vehicle for vehicle in self.__vehicles if vehicle.engine.maximum_speed <= max_speed]

    def get_type_compustion(self, combustible_type: str) -> List[Vehicle]:
        return [vehicle for vehicle in self.__vehicles if vehicle.engine.combustion_type == combustible_type]

    def add_vehicle(self, vehicle: Vehicle):
        self.__vehicles.append(vehicle)

class ProxyCatalog:
    def __init__(self):
        self.__real_catalog = Catalog()

    def get_all_vehicles(self) -> List[Vehicle]:
        return self.__real_catalog.get_all_vehicles()

    def get_price_by_range(self, min_price: float, max_price: float) -> List[Vehicle]:
        return self.__real_catalog.get_price_by_range(min_price, max_price)
    
    def search_max_speed(self, max_speed: int) -> List[Vehicle]:
        return self.__real_catalog.search_max_speed(max_speed)

    def get_type_compustion(self, combustible_type: str) -> List[Vehicle]:
        return self.__real_catalog.get_type_compustion(combustible_type)

    def add_vehicle(self, vehicle: Vehicle):
        self.__real_catalog.add_vehicle(vehicle)

    def delete_vehicle(self, vehicle: Vehicle):
        self.__real_catalog.__vehicles.remove(vehicle)