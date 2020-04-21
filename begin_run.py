import sys
from utils import parse_raw_temps

def begin_run():
	input_file_path = "./input/" + sys.argv[1]
	temps = []
	with open(input_file_path, 'r') as f:
		temps = parse_raw_temps(f, 30, False)

if __name__ == "__main__":
	begin_run()