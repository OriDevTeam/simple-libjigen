## System Imports


## Application Imports


## Library Imports


def convert(unified: bool, source: str, target: str) -> Exception | None:

	if unified:
		return convert_unified(source, target)
	
	return convert_parted(source, target)


def convert_unified(source: str, target: str) -> Exception | None:
	
	pass


def convert_parted(source: str, target: str) -> Exception | None:
	
	pass
