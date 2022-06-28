## System Imports
from argparse import ArgumentParser


## Application Imports
from simple_libjigen.converters.map import converter
from simple_libjigen.converters.script import racedata


## Library Imports


def setup_args():
	args_parser = ArgumentParser(prog='simple-libjigen, the tool for simple data format handling')
	subparsers = args_parser.add_subparsers(help='Specify which format to handle', dest='format')
	
	script_parser = subparsers.add_parser('script', help='Handles the script data format')
	script_subparsers = script_parser.add_subparsers(help='Specify which subset format to handle', dest='script')
	
	script_racedata_script_parser = script_subparsers.add_parser('racedata', help='Handles the racedata data format')
	script_racedata_script_parser.add_argument(
		'-s', '--source', type=str, help='Source location of the racedata data'
	)
	script_racedata_script_parser.add_argument(
		'-p', '--parted', type=bool, help='Specifies if the source data is parted or unified'
	)
	
	map_parser = subparsers.add_parser('map', help='Handles the map data format')
	# map_parser.add_argument('-p', type=bool, help='Specifies if the source data is parted or unified')
	map_parser.add_argument(
		'-s', '--source', type=str, help='Source location of the racedata data'
	)
	
	args_parser.add_argument(
		'-ff', '--from-format', type=str, help='Expected format of the given data',
		choices=['legacy', 'json']
	)
	
	args_parser.add_argument(
		'-c', '--convert', type=str, help='Convert the given data to a specific format',
		choices=['legacy', 'json']
	)
	args_parser.add_argument(
		'-o', '--output', type=str, help='Outputs to the given path/directory'
	)
	
	return args_parser


def run_commands(args):
	if args.format == 'map':
		converter.convert(args.source, args.output, args.from_format, args.convert)
	
	elif args.format == 'script':
		if args.script:
			racedata.convert(not args.parted, args.source, args.output, args.from_format, args.convert)


if __name__ == '__main__':
	parser = setup_args()
	args = parser.parse_args()
	
	print(parser.description, end='\n\n')
	print(args)  # TODO: Remove this printing when initial developing is done


