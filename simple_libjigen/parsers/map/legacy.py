## System Imports
import re
import glob
from pathlib import Path


## Application Imports
from simple_libjigen.factory import factory
from simple_libjigen.data.map.map import Map, MapSetting, MapProperty
from simple_libjigen.parsers.script.legacy import ScriptLegacyFormatParser, GroupScriptLegacyFormatParser
from simple_libjigen.data.map.chunk import MapChunk, ChunkArea, ChunkAmbienceArea, ChunkProperty, ChunkObject


## Library Imports


@factory.register
class MapLegacyFormatParser:
	
	@classmethod
	def parse(cls, directory: str):
		map_data = Map(
			settings=cls.parse_setting(f'{directory}/setting.txt'),
			property=cls.parse_property(f'{directory}/mapproperty.txt'),
			chunks=cls.parse_chunks(f'{directory}')
		)
		
		return map_data
	
	@classmethod
	def parse_setting(cls, path: str) -> MapSetting:
		content = Path(path).read_text()
		fields = ScriptLegacyFormatParser.parse(content)
		script_type = fields.pop('ScriptType', None)
		
		if 'MapSetting' != script_type:
			raise AttributeError(f"Map setting script type should be 'MapSetting', got {script_type} instead")
		
		return MapSetting(**fields)
	
	@classmethod
	def parse_property(cls, path: str) -> MapProperty:
		fields = ScriptLegacyFormatParser.parse(Path(path).read_text())
		script_type = fields.pop('ScriptType', None)
		
		if 'MapProperty' != script_type:
			raise AttributeError(f"Map setting script type should be 'MapProperty', got {script_type} instead")
		
		return MapProperty(**fields)
	
	@classmethod
	def parse_chunks(cls, directory: str) -> list[MapChunk]:
		chunk_dirs = glob.glob(f'{directory}/' + ('[0-9]' * 6))
		
		chunks = [ChunkLegacyFormatParser.parse(chunk_dir) for chunk_dir in chunk_dirs]
		
		return chunks


class ChunkLegacyFormatParser:
	
	@classmethod
	def parse(cls, directory: str) -> MapChunk:
		chunk_area = cls.parse_area(f'{directory}/areadata.txt')
		chunk_ambience = cls.parse_ambience(f'{directory}/areaambiencedata.txt')
		chunk_property = cls.parse_property(f'{directory}/areaproperty.txt')
		
		return MapChunk(chunk_area, chunk_ambience, chunk_property)
	
	@classmethod
	def parse_area(cls, path: str) -> ChunkArea:
		pattern = r'^Start\s.*?Object(.*?)\n.*?\s.*?(.*?)\n.*?(.*?)\n.*?(.*?)\s.*?(.*?)\n.*?(.*?)\n.*?End\s.*?Object$'
		content = Path(path).read_text()
		
		if 'AreaDataFile' not in content:
			raise AttributeError(f"File content does notcontain the definition 'AreaDataFile', path {path}")
		
		chunk_objects = []
		
		for match in re.finditer(pattern, content, re.MULTILINE):
			fields = match.groups()
			
			x, y, z = fields[1].lstrip().split()
			
			if '#' in fields[4]:
				yaw, pitch, roll = fields[4].strip().split('#')
			else:
				yaw, pitch, roll = 0, 0, fields[3]
			
			chunk_object = ChunkObject(
				id=fields[0],
				x=float(x),
				y=float(y),
				z=float(z),
				crc32=int(fields[2].strip()),
				yaw=float(yaw),
				pitch=float(pitch),
				roll=float(roll),
				height_delta=float(fields[5].strip())
			)
			
			chunk_objects.append(chunk_object)
		
		return ChunkArea(Objects=chunk_objects)

	@classmethod
	def parse_ambience(cls, path: str) -> ChunkAmbienceArea:
		content = Path(path).read_text()
		
		if 'AreaAmbienceDataFile' not in content:
			raise AttributeError(f"File content does notcontain the definition 'AreaDataFile', path {path}")
		
		fields = GroupScriptLegacyFormatParser.parse(content)
		
		return ChunkAmbienceArea(**fields)
	
	@classmethod
	def parse_property(cls, path: str) -> ChunkProperty:
		content = Path(path).read_text()
		
		fields = ScriptLegacyFormatParser.parse(content)
		script_type = fields.pop('ScriptType', None)
		
		if 'AreaProperty' != script_type:
			raise AttributeError(f"Area property script type should be 'AreaProperty', got {script_type} instead")
		
		return ChunkProperty(**fields)
	
