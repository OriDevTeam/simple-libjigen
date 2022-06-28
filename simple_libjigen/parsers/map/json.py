## System Imports


## Application Imports


## Library Imports
from simple_libjigen.data.map.map import Map
from simple_libjigen.factory import factory


@factory.register
class JsonFormat:
	
	@classmethod
	def parse_output(cls, map_directory: str, target_directory: str):
		pass
	
	@classmethod
	def dump(cls, map_data: Map) -> str:
		pass
	
