import sys
from parse_temps import parse_raw_temps, get_values_count
from piecewise_linear_interpolation import compute_slope, compute_y_intercept


def begin_run():
	input_file_path = "./input/" + sys.argv[1]
	includes_units = sys.argv[2] == "yes"  # set to False for files without units
	temps = []
	with open(input_file_path, 'r') as f:
		temps = list(parse_raw_temps(f, 30, units=includes_units))
	print(compute_slope(1, 1, 2, 2))
	print("y intercept: ", compute_y_intercept(2,5,3))

	temp_values = {}
	rows = get_values_count(input_file_path)
	columns = 2

	for i in range(0, 4):
		temp_values["core_{0}".format(i)] = [[0 for j in range(columns)] for x in range(rows)]

	print(temp_values)

if __name__ == "__main__":
	begin_run()