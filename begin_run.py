import sys
from parse_temps import parse_raw_temps

def begin_run():
	input_file_path = "./input/" + sys.argv[1]
	includes_units = sys.argv[2] == "yes"  # set to False for files without units
	temps = []
	with open(input_file_path, 'r') as f:
		temps = parse_raw_temps(f, 30, units=includes_units)
		print(*temps, sep='\n') # * will unpack the list
if __name__ == "__main__":
	begin_run()