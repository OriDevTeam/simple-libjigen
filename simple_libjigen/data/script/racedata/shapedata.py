## System Imports
from dataclasses import dataclass


## Application Imports


## Library Imports


@dataclass(slots=True, order=True)
class ShapeDataValue:
	
	ShapeIndex: int
	Model: str
	SourceSkin: str
	TargetSkin: str


@dataclass(slots=True, order=True)
class ShapeData:
	
	PathName: str
	ShapeDataCount: int
	
	Groups: list[ShapeDataValue]
