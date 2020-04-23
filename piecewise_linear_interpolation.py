import sys
from typing import (List, TextIO)

def compute_slope(x1: int, y1: int, x2: int, y2: int) -> float:
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

def compute_y_intercept(x: int, m: float, y: int) -> int:
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

def compute_piecewise_linear_interpolation(matrix: List[List[float]], step_size: int) -> List[List[float]]:
	"""
	Takes a matrix for a given core and computes the piecewise linear itnerpolation for each time step
	
	Args:
		matrix: The matrix for a given core
		step_size: The step size for sampling (always 30 in our case)

	Yields:
		A list of values containing the piecewise linear interpolation (x0, y intercept, and slope)
	"""
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

def write_to_file(systems_linear_equations: List[List[float]], output_file: TextIO, step_size: int) -> None:
	"""
	Writes the list of results from computing the piecewise linear interpolation to an output file

	Args:
		systems_linear_equations: The results from computing the piecewise linear interpolation
		output_file: The file to write the results to
		step_size: The step size of the sampling rate (always 30 for our case)
	
	Yields:
		None
	"""
	count = 0
	for value in systems_linear_equations:
		x_value = "{:.4f}".format(round(value[2], 4))
		c_value = "{:.4f}".format(round(value[1], 4))
		output_file.write(f'{value[0]} <= x < {value[0] + step_size}; \t y_{count} =  {c_value} + {x_value}x\t\tinterpolation \n')
		count += 1