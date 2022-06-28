## System Imports
from dataclasses import dataclass, field

## Application Imports
from typing import Optional

from simple_libjigen.data.script.racedata.hairdata import HairData
from simple_libjigen.data.script.racedata.shapedata import ShapeData


## Library Imports


@dataclass(slots=True, order=True)
class RaceData:

	BaseModelFileName: str
	HairData: Optional[HairData] = None
	ShapeData: Optional[ShapeData] = None
	

