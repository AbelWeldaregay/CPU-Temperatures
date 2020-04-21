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