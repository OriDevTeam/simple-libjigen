## System Imports
import re
from pathlib import Path


## Application Imports
from simple_libjigen.factory import factory
from simple_libjigen.data.script.racedata import RaceData, HairData, ShapeData
from simple_libjigen.parsers.script.legacy import GroupScriptLegacyFormatParser


## Library Imports


@factory.register
class RaceDataLegacyParser:
	
	@classmethod
	def parse_parted(cls, directory: str) -> RaceData:
		race_data = RaceDataLegacyFormatParser.parse_race_data(f'{directory}/racedata.msm')
		race_data.HairData = RaceDataLegacyFormatParser.parse_hair_data(f'{directory}/hairdata.msm')
		race_data.ShapeData = RaceDataLegacyFormatParser.parse_shape_data(f'{directory}/shapedata.msm')
		
		return race_data
	
	@classmethod
	def parse_unified(cls, path: str) -> RaceData:
		race_data = RaceDataLegacyFormatParser.parse_race_data(path)
		
		return race_data


class RaceDataLegacyFormatParser:
	
	@classmethod
	def parse_race_data(cls, path: str) -> RaceData:
		content = Path(path).read_text()
		fields = GroupScriptLegacyFormatParser.parse(content)
		script_type = fields.pop('ScriptType')
		
		if 'RaceDataScript' != script_type:
			raise AttributeError(f"Script type should be 'RaceDataScript', got {script_type} instead")
		
		return RaceData(**fields)
	
	@classmethod
	def parse_hair_data(cls, path: str) -> HairData:
		content = Path(path).read_text()
		fields = GroupScriptLegacyFormatParser.parse(content)['HairData']
		
		fields['Groups'] = {}
		pop_fields = []
		for key, value in fields.items():
			if re.match(r'HairData[0-9]+', key):
				fields['Groups'][key] = value
				pop_fields.append(key)
		
		for field in pop_fields:
			fields.pop(field)
		
		return HairData(**fields)
	
	@classmethod
	def parse_shape_data(cls, path: str) -> ShapeData:
		content = Path(path).read_text()
		fields = GroupScriptLegacyFormatParser.parse(content)['ShapeData']
		# script_type = fields.pop('ScriptType')
		
		fields['Groups'] = {}
		pop_fields = []
		for key, value in fields.items():
			if re.match(r'ShapeData[0-9]+', key):
				fields['Groups'][key] = value
				pop_fields.append(key)
		
		for field in pop_fields:
			fields.pop(field)
		
		return ShapeData(**fields)
	
