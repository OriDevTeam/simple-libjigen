## System Imports
from dataclasses import dataclass


## Application Imports


## Library Imports
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(slots=True, order=True)
class ChunkProperty:

	AreaName: str
	NumWater: str


@dataclass_json
@dataclass(slots=True, order=True)
class ChunkAmbienceArea:

	ObjectCount: int


@dataclass(slots=True, order=True)
class ChunkObject:
	
	id: int
	
	x: float
	y: float
	z: float
	
	crc32: int
	
	yaw: float
	pitch: float
	roll: float
	
	height_delta: float


@dataclass_json
@dataclass(slots=True, order=True)
class ChunkArea:

	Objects: list[ChunkObject]
	

@dataclass(slots=True, order=True)
class MapChunk:
	
	area: ChunkArea
	ambience: ChunkAmbienceArea
	property: ChunkProperty
	
