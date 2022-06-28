## System Imports


## Application Imports
import main


## Library Imports


def tests_main(arguments: list[str]):
	parser = main.setup_args()
	args = parser.parse_args(arguments)
	
	main.run_commands(args)

