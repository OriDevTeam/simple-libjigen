## System Imports
import json
from dataclasses import asdict


## Application Imports
from simple_libjigen.factory import factory
from simple_libjigen.data.script.racedata import RaceData


## Library Imports


@factory.register
class RaceDataJSONParser:
	
	@classmethod
	def dump_unified(cls, race_data: RaceData) -> str:
		data = asdict(race_data)
		
		return json.dumps(data, indent=4)
