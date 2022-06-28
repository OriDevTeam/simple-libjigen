## System Imports
from dataclasses import dataclass


## Application Imports


## Library Imports


@dataclass(slots=True, order=True)
class HairDataValue:

	HairIndex: int
	Model: str
	SourceSkin: str
	TargetSkin: str


@dataclass(slots=True, order=True)
class HairData:
	
	PathName: str
	HairDataCount: str
	Groups: list[HairDataValue]
	
