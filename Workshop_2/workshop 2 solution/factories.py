
#abc for saying that we are using abstract clases


from abc import ABC
from engines import ElectricEngine, GasEngine

class AbstractEngineFactory(ABC):
	def create_electric_engine(self):
		pass
	def create_gas_engine(self):
		pass

class HighEngineFactory(AbstractEngineFactory):
	
	def create_electric_engine(self):
		pass
	
	def create_gas_engine(self):
		pass

class PoorEngineFactory(AbstractEngineFactory):
	def create_electric_engine(self):
		return ElectricEngine(
			torque= 200,
			maximun_speed= 460,
			dimensions= "200x200x200",
			power =200,
			stability = "high"
			weight= 100.9
			):
	
	def create_gas_engine(self):
		pass