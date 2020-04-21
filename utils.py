import sys
from typing import *
from typing import TextIO

def parse_raw_temps(original_temps: TextIO,
                    step_size: int=30, units: bool=True) -> Iterator[Tuple[float, List[float]] ]:
    """
    Take an input file and time-step size and parse all core temps.

    :param original_temps: an input file
    :param step_size:      time-step in seconds
    :param units: True if the input file includes units and False if the file
                  includes only raw readings (no units)

    :yields: A tuple containing the next time step and a List containing _n_
             core temps as floating point values (where _n_ is the number of
             CPU cores)
             Ex Matrix: 
             Time (sec)	Core 0	Core 1	Core 2	Core 3
			 0			61.0	63.0	50.0	58.0
			 30			80.0	81.0	68.0	77.0
			 60			62.0	63.0	52.0	60.0
			 120		83.0	82.0	70.0	79.0
			 180		68.0	69.0	58.0	65.0
    """
    result = []
    # result.append(original_temps.readline().strip().split(" ").insert(0, 0))
    first_line = original_temps.readline()
    first_line = first_line.strip().split(" ")
    first_line.insert(0, 0)
    i = 1
    curr_step = step_size
    result.append(first_line)
    for line in original_temps:
    	stripped_line = line.strip()
    	line_list = stripped_line.split(" ")
    	line_list.insert(0, curr_step)
    	result.append(line_list)
    	if i % 2 == 0:
    		step_size *= 2
    	curr_step += step_size
    	i += 1

    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in result]))