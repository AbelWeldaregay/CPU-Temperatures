import sys
import os
from typing import (List, TextIO)

def multiply(A: List[List[int]], B: List[List[int]]):
	"""
    Multiplies two given matrix
    Parameters
    ----------
    arg1 : A 
		The first matrix to be multiplied
	arg2: B
		The second matrix to be multiplied
    Returns
    -------
    List
        The result of A*B
    """
	result = []
	sum = 0
	for i in range(0, len(A)):
		result.append([])
		for j in range(0, len(B[0])):
			for k in range(0, len(A[0])):
				sum += A[i][k] * B[k][j]
			result[i].append(sum)
	return result

def compute_x(A: List[List[int]]):
	"""
	Builds the X matrix using the algorithm from the lecture notes
	1. The first column is defined by taking each x value and plugging it into y=1.
	2. The second column is defined by taking each x value and plugging it into y=x. 2
	3. The third column is defined by taking each x value and plugging it into y=x2.
	"""
	result = []
	for i in range(0, len(A)):
		temp = []
		temp.append(1)
		temp.append(A[i][0])
		result.append(temp)

	return result


def compute_y(A: List[List[int]]) -> List[List[int]]:
	"""
	Builds the Y matrix using the algorithm from the lecture notes
	"""
	result = []
	for i in range(0, len(A)):
		temp = []
		temp.append(A[i][1])
		result.append(temp)
	return result

def scale_row(A: List[List[int]], row_idx: int, num_cols: int, s: int) -> List[List[int]]:
	"""
	Scales row by a given scaler s
	"""
	for j in range(num_cols):
		A[row_idx][j] = A[row_idx][j] / s
	return A

def transpose(A: List[List[int]]) -> List[List[int]]:
	"""
	Computes the transpose of a given matrix
	"""
	return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))] 

def find_largest_row_by_col(A: List[List[int]], col_index: int, num_rows: int) -> int:
	"""
	Finds the largest row for a given column
	"""
	largest = A[0][col_index]
	largest_row_idx = 0
	for i in range(num_rows):
		if A[i][col_index] > largest:
			largest = A[i][col_index]
			largest_row_idx = i
	return largest_row_idx

def swap_row(matrix: List[List[int]], row_one: int, row_two: int) -> None:
	"""
	Swaps two given rows of a matrix
	"""
	temp = matrix[row_one]
	matrix[row_one] = matrix[row_two]
	matrix[row_two] = temp


def compute_global_least_square_approximation(matrix: List[List[int]], output_file) -> List[List[int]]:
		x = compute_x(matrix)
		y = compute_y(matrix)
		x_transpose = transpose(x)
		x_transpose_x = multiply(x_transpose, x)
		x_transpose_y = multiply(x_transpose, y)
		augmented_matrix = augment(x_transpose_x, x_transpose_y)
		solution_matrix = gaussian(augmented_matrix)
		write_to_file(solution_matrix, output_file, x[len(x) - 1][1])
		return solution_matrix

def write_to_file(solution_matrix: List[List[int]], output_file: TextIO, max_time: int) -> List[List[int]]:
	c0 = round(solution_matrix[0][2], 6)
	c1 = round(solution_matrix[1][2], 6)
	output_file.write(f'0 <= x < {max_time}; y = {c0} + {c1}x; least-squares \n ')

def eliminate(A: List[List[int]], src_row_idx: int, num_cols: int, num_rows: int):
	"""
	Eliminates row by doing subtraction operations
	"""
	start_col = src_row_idx
	for i in range(src_row_idx + 1, num_rows):
		s = A[i][start_col]
		for j in range(start_col, num_cols):
			A[i][j] = A[i][j] - (s*A[src_row_idx][j])
		A[i][start_col] = 0
	return A

def augment(x_transpose_x: List[List[int]], x_transpose_y: List[List[int]]):
	"""
	Computes the augmented matrix to be used
	in gaussian elimination
	"""
	column_count = len(x_transpose_x[0]) - 1
	result_row_count = len(x_transpose_x) + 1
	result_column_count = len(x_transpose_x[0])
	result = [[0 for i in range(result_row_count)] for j in range(result_column_count)]
	for i in range(len(x_transpose_x)):
		for j in range(len(x_transpose_x[0])):
			result[i][j] = x_transpose_x[i][j]
			if j == column_count:
				result[i][j+1] = x_transpose_y[i][0]
	return result

def gaussian(matrix: List[List[int]]) -> List[List[int]]:
    """
    Solves matrix using gaussian elimination
    1. itterate through the rows
    2. find the max index
    3. swap rows i and max index
    4. scale the current row
    5. do subtraction operations to eliminate row
    """
    n = len(matrix)
    numColumns = len(matrix[0])
    # Iterate through all rows
    for i in range(0, n):   
        
        max_idx = find_largest_row_by_col(matrix, i, n)

        swap_row(matrix, i, max_idx)

        scale_row(matrix, i, numColumns, matrix[i][i])

        eliminate(matrix, i, numColumns, n)

    return matrix

def back_solve(matrix: List[List[int]]) -> List[int]:
	"""
	Starts from the end and backsolves to find the identity matrix
	"""
	aug_col_idx = len(matrix)
	last_row = len(matrix) - 1


	for i in range(last_row, 0, -1):
		for j in range(i - 1, -1, -1):
          
			s = matrix[j][i]

			matrix[j][i] = matrix[j][i] - (s * matrix[i][i])
			matrix[j][aug_col_idx] = matrix[j][aug_col_idx] - (s * matrix[i][aug_col_idx])

	return matrix
