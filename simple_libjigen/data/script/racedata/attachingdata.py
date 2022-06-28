## System Imports
from dataclasses import dataclass


## Application Imports


## Library Imports

@dataclass(slots=True, order=True)
class SphereDataValue:

	Radius: float
	Position: tuple[float, float, float]


@dataclass(slots=True, order=True)
class AttachingDataValue:

	AttachingDataType: int
	IsAttaching: int
	AttachingModelIndex: int
	AttachingBoneName: int
	CollisionType: int
	SphereDataCount: int
	

@dataclass(slots=True, order=True)
class AttachingData:

	AttachingDataCount: int
	
	