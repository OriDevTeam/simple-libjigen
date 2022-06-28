## System Imports
from dataclasses import dataclass


## Application Imports
from simple_libjigen.data.map.chunk import MapChunk


## Library Imports
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(slots=True, order=True)
class MapProperty:
	
	MapType: str


@dataclass_json
@dataclass(slots=True, order=True)
class MapSetting:
	
	CellScale: int
	HeightScale: float
	ViewRadius: int
	MapSize: tuple[int, int]
	BasePosition: tuple[int, int]
	TextureSet: str
	Environment: str


@dataclass(slots=True, order=True)
class Map:
	
	settings: MapSetting
	property: MapProperty
	chunks: list[MapChunk]

