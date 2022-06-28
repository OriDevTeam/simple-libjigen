## System Imports


## Application Imports
import dev_tests


## Library Imports


if __name__ == '__main__':
	dev_tests.tests_main(r'--from-format=legacy --convert=json '
						 r'--output=unified-sample.json '
						 r'script racedata --source=../tests/data/racedata/legacy/unified-sample.msm '
						 .split())
