import sys

def compute_slope(x1, y1, x2, y2):
	"""
	Computes the slope of two given points
	Formula:
		m = rise / run -> change in y / change in x
	Args:
		x1: X value of the first point
		y1: Y value of the first point
		x2: X value of second point
		y2: Y value of the second point
	Yields:
		Returns the slope of the two given points
	"""
	return (y2 - y1) / (x2 - x1)

def compute_y_intercept(x, m, y):
	"""
	Computes the y intercept given x, m (slope), and y values
	Uses classical formula y = mx + b and solves for b (y)
	
	Args:
	x: the x value
	m: the current slope
	y: the y value

	Yields:
	The y intercept

	"""

	return y - (m*x)

def compute_piecewise_linear_interpolation(matrix, step_size):
	systems_linear_equations = []
	for i in range(0, len(matrix) - 1):
		x0 = matrix[i][0]
		x1 = matrix[i + 1][0]
		y0 = matrix[i][1]
		y1 = matrix[i + 1][1]

		slope = compute_slope(x0, y0, x1, y1)
		y_intercept = compute_y_intercept(x0, slope, y0)

		y_intercept_slope = (x0, y_intercept, slope)
		systems_linear_equations.append(y_intercept_slope)

	return systems_linear_equations

def write_to_file(systems_linear_equations, output_file, step_size):
	count = 0
	for value in systems_linear_equations:
		x_value = "{:.4f}".format(round(value[2], 4))
		c_value = "{:.4f}".format(round(value[1], 4))
		output_file.write(f'{value[0]} <= x < {value[0] + step_size}; \t y_{count} =  {c_value} + {x_value}x \t interpolation \n')
		count += 1