import sys
from parse_temps import parse_raw_temps, get_values_count
from piecewise_linear_interpolation import compute_slope, compute_y_intercept
from utils import build_cpu_temp_dict, get_raw_temps
import matrix_solver.utils as matrix_solver

def begin_run():
	input_file_path = "./input/" + sys.argv[1]
	includes_units = sys.argv[2] == "yes"  # set to False for files without units
	step_size = 30
	# original_temps = get_raw_temps(input_file_path, step_size, includes_units)
	rows = get_values_count(input_file_path)
	columns = 2

	temps_dict = build_cpu_temp_dict(rows, columns, None, step_size, input_file_path, includes_units)

	for i in range(0, 4):
		output_file_name = "output-core-{}.txt".format(i)
		solution_matrix = matrix_solver.compute_global_least_square_approximation(temps_dict["core_{}".format(i)], output_file_name)
		# matrix_solver.write_to_file(solution_matrix, output_file_name, x[len(x) - 1][1])
if __name__ == "__main__":
	begin_run()