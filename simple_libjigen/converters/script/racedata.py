## System Imports
import os.path


## Application Imports
from pathlib import Path

from simple_libjigen.parsers.script import racedata


## Library Imports


def convert(unified: bool, source: str, target: str, from_format: str, to_format: str) -> Exception | None:

	if unified:
		return convert_unified(source, target, from_format, to_format)
	
	return convert_parted(source, target, from_format, to_format)


def convert_unified(source: str, target: str, from_format: str, to_format: str) -> Exception | None:
	formats = racedata.parsers()
	
	if from_format not in formats:
		raise AttributeError()
	
	if to_format not in formats:
		raise AttributeError()
	
	if not target:
		raise AttributeError(f'A target path for saving was not given')
	
	path = Path(target)
	
	from_parser = racedata.parser(from_format)
	racedata_data = from_parser.parse_unified(source)
	
	to_parser = racedata.parser(to_format)
	racedata_target = to_parser.dump_unified(racedata_data)
	
	with open(path, 'w') as f:
		f.write(racedata_target)
	
	return racedata_target


def convert_parted(source: str, target: str, from_format: str, to_format: str) -> Exception | None:
	
	pass
