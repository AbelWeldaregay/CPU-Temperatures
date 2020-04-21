import sys
from parse_temps import parse_raw_temps
from piecewise_linear_interpolation import compute_slope
def begin_run():
	input_file_path = "./input/" + sys.argv[1]
	includes_units = sys.argv[2] == "yes"  # set to False for files without units
	temps = []
	with open(input_file_path, 'r') as f:
		temps = list(parse_raw_temps(f, 30, units=includes_units))
	print(compute_slope(1, 1, 2, 2))
if __name__ == "__main__":
	begin_run()