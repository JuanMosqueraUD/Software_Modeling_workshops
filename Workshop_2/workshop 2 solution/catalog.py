# lista de objetos typing

from typing import List
from vehicles import Vehicle
class Catalog:

	def __init__(self):
		self.vehicles = List[Vehicle]
	
	def __new__(cls):
		if not hasattr(cls, "instance"):
			cls.instance = super(Catalog,cls).__new__(cls)

		return cls.instance
	def get_all_vehicles(self):
		return self.vehicles
	
	def get_price_by_range(self,min_price,max_price):
		return [vehicle for vehicle in self.vehicle if min_price <= vehicle.price <=max_price]
		