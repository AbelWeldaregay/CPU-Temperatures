import sys
from parse_temps import parse_raw_temps, get_values_count
from piecewise_linear_interpolation import compute_slope, compute_y_intercept
from utils import build_cpu_temp_dict, get_raw_temps

def begin_run():
	input_file_path = "./input/" + sys.argv[1]
	includes_units = sys.argv[2] == "yes"  # set to False for files without units
	step_size = 30
	original_temps = get_raw_temps(input_file_path, step_size, includes_units)
	rows = get_values_count(input_file_path)
	columns = 2

	print(build_cpu_temp_dict(rows, columns, original_temps, step_size))

if __name__ == "__main__":
	begin_run()