## System Imports
import unittest


## Application Imports


## Library Imports
from simple_libjigen.parsers.script.racedata.legacy import RaceDataLegacyParser


class RaceDataParsingOperations(unittest.TestCase):
	
	def test_legacy_parted_parsing(self):
		directory = 'data/racedata/legacy/parted/'
		
		race_data = RaceDataLegacyParser.parse_parted(directory)
		
		self.assertIsNotNone(race_data)
	
	def test_legacy_unified_parsing(self):
		path = 'data/racedata/legacy/unified-sample.msm'
		
		race_data = RaceDataLegacyParser.parse_unified(path)
		
		self.assertIsNotNone(race_data)
	
	def test_json_parted_parsing(self):
		pass
	
	def test_json_unified_parsing(self):
		pass


class RaceDataConvertingOperations(unittest.TestCase):
	
	def test_convert_from_legacy_to_json(self):
		raise NotImplementedError
	
	def test_convert_from_json_to_legacy(self):
		raise NotImplementedError


if __name__ == '__main__':
	unittest.main()
	
