## System Imports


## Application Imports
import dev_tests


## Library Imports


if __name__ == '__main__':
	dev_tests.tests_main('--from-format=legacy --convert=json '
						 'map --source=""'.split())
