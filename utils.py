import sys
from parse_temps import parse_raw_temps
from typing import ( List, Iterator, List, Tuple, Dict )

def get_raw_temps(input_file_path: str, step_size: int, includes_units: bool) -> List[Tuple[float, List[float]]]:
	"""
	Opens the file and reads the raw temps of the given file
	
	Args:
		input_file_path: The file path of the file to be parsed
		step_size: The step size
	
	Yields
		Original temp values
	"""
	original_temps = []
	step_size = 30
	with open(input_file_path, 'r') as f:
		original_temps = list(parse_raw_temps(f, step_size, units=includes_units))

	return original_temps

def build_cpu_temp_dict(rows: int, columns: int, step_size: int, input_file_path: str, includes_units: bool) -> Dict[str, List[float]]:
	"""
	Builds the CPU temparature dictionary using the core as 
	the key and a list of values as the time step and temparature
	
	Args:
		rows: The number of rows in the file
		columns: the number of columns (will always be 2 in this case)
		original_temps: The original temp values from reading the input file
		step_size: The step size (will always be 30 in this case)
	Yields:
		A dictionary in the format [core_n : [time step, temperature]]
	"""

	with open(input_file_path, 'r') as input_file:
		temperature_dict = {}
		for i in range(0, 4):
			temperature_dict["core_{0}".format(i)] = [[0 for j in range(columns)] for x in range(rows)]

		for value in parse_raw_temps(input_file, step_size=step_size, units=includes_units):
			row = int( value[0] / step_size)
			for i in range(0, 4):
				temperature_dict["core_{0}".format(i)][row][0] = value[0]
				temperature_dict["core_{0}".format(i)][row][1] = value[1][i]

	return temperature_dict