## System Imports
import ast
import re
from typing import Any


## Application Imports
from simple_libjigen.factory import factory


## Library Imports


@factory.register
class ScriptLegacyFormat:
	
	@classmethod
	def parse_output(cls, map_directory: str, format_directory: str):
		pass


class ScriptLegacyFormatParser:
	
	@classmethod
	def parse(cls, content: str) -> dict:
		data: dict = {}
		
		for line in content.split('\n'):
			if '{' in line or '}' in line:
				continue
			
			kv = cls.parse_field(line)
			if not kv:
				continue
				
			data[kv[0]] = kv[1]
			
		return data
	
	@classmethod
	def parse_field(cls, line: str) -> tuple[str, Any] | None:
		kv: list[str] = line.split(maxsplit=1)
		
		if len(kv) < 2:
			return None
		
		key: str = kv[0]
		value = kv[1]
		
		if '\t' in value or ' ' in value:
			value = [float(v) for v in value.split()]
		
		elif value.isnumeric():
			value = int(value)
		
		elif '"' in value:
			value = str(value.split('"')[1].split('"')[0])
		
		elif re.match(r'[+-]?[\d.]+', value):
			value = float(value)
		
		return key, value
	

class GroupScriptLegacyFormatParser:

	@classmethod
	def parse(cls, content: str) -> dict:
		contents = content.split('\n')
		lines = '{'
		
		group_index = 0
		idx = 0
		for line in contents:
			if '{' in line:
				lines += line + '\n'
				group_index += 1
				continue
				
			if '}' in line:
				lines += line + ',\n'
				
				if group_index - 1 == 0:
					group_index -= 1
					lines += '},'
				continue
			
			if len(line.strip()) == 0:
				continue
			
			idx += 1
			
			kv: list[str] = line.split(maxsplit=1)
			
			if kv[0].lower() == 'group':
				lines += f'"{kv[1]}":'
				group_index += 1
				continue
			
			lines += f'"{kv[0]}":{kv[1]}'
			
			if '{' not in contents[idx+1] or '}' not in contents[idx+1]:
				lines += ',\n'
				continue
			
			lines += '\n'
		
		lines += '}'
		
		return ast.literal_eval(lines)
		
