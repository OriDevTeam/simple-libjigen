## System Imports


## Application Imports


## Library Imports
from simple_libjigen.parsers import map


def convert(source: str, target: str, from_format: str, to_format: str) -> Exception | None:
	formats = map.parsers()
	
	if from_format not in formats:
		raise AttributeError()
	
	if to_format not in formats:
		raise AttributeError()
	
	from_parser = map.parser(from_format)
	map_data = from_parser.parse(source)
	
	
	
	return map_data
