import sys
import os
from parse_temps import get_values_count
import piecewise_linear_interpolation
from utils import build_cpu_temp_dict
import matrix_solver.utils as matrix_solver
"""
The entry point of the program
"""
def begin_run():
	input_file_path = "./input/" + sys.argv[1]
	includes_units = sys.argv[2] == "yes"  # set to False for files without units
	step_size = 30
	# original_temps = get_raw_temps(input_file_path, step_size, includes_units)
	rows = get_values_count(input_file_path)
	columns = 2

	temps_dict = build_cpu_temp_dict(rows, columns, step_size, input_file_path, includes_units)
	for i in range(0, 4):
		output_file_name = "output/output-core-{}.txt".format(i)
		if os.path.exists(output_file_name):
			os.remove(output_file_name)
		output_file = open(output_file_name, 'a')
		solution_matrix = matrix_solver.compute_global_least_square_approximation(temps_dict["core_{}".format(i)], output_file)
		systems_linear_equations = piecewise_linear_interpolation.compute_piecewise_linear_interpolation(temps_dict["core_{}".format(i)], step_size)
		piecewise_linear_interpolation.write_to_file(systems_linear_equations, output_file, step_size)
		output_file.close()

if __name__ == "__main__":
	begin_run()