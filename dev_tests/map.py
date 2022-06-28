## System Imports


## Application Imports
import dev_tests

## Library Imports


if __name__ == '__main__':
	dev_tests.tests_main(r'--from-format=legacy --convert=json '
						 r'output=../tests/data/map/json/village-legacy/'
						 r'map --source=../../../Rust/Bevy/test_data/maps/village-legacy/'
						 .split())
