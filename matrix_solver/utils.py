import sys
import os

def multiply(lhs, rhs):

    """
    Take two matrices and multiply them

    Args:
        lhs - (List) representing the left matrix to multiply 
        rhs - (List) representing the right matrix to multiply

        Yields:
            Result of multiplying the right matrix by the left matrix
 
    """

    sum = 0
    result = []
    lhsRows = len(lhs)
    rhsColumns = len(rhs[0])

    n = len(lhs[0])
   
    for i in range(0, lhsRows):
        result.append([]);
        for j in range(0, rhsColumns):
            # result[i].append([])
            for k in range(0, n):
                sum += lhs[i][k] * rhs[k][j]
            result[i].append(sum)
            sum = 0

    return result

def compute_x(A):
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


def compute_y(A):
	"""
	Builds the Y matrix using the algorithm from the lecture notes
	"""
	result = []
	for i in range(0, len(A)):
		temp = []
		temp.append(A[i][1])
		result.append(temp)
	return result

def scale_row(A, row_idx, num_cols, s):
	"""
	Scales row by a given scaler s
	"""
	for j in range(num_cols):
		A[row_idx][j] = A[row_idx][j] / s
	return A

def transpose(A):
	"""
	Computes the transpose of a given matrix
	"""
	return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))] 

def find_largest_row_by_col(A, col_index, num_rows):
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

def swap_row(matrix, row_one, row_two):
	"""
	Swaps two given rows of a matrix
	"""
	temp = matrix[row_one]
	matrix[row_one] = matrix[row_two]
	matrix[row_two] = temp


def compute_global_least_square_approximation(matrix, output_file_name):
		x = compute_x(matrix)
		y = compute_y(matrix)
		x_transpose = transpose(x)
		x_transpose_x = multiply(x_transpose, x)
		x_transpose_y = multiply(x_transpose, y)
		augmented_matrix = augment(x_transpose_x, x_transpose_y)
		solution_matrix = gaussian(augmented_matrix)
		write_to_file(solution_matrix, output_file_name, x[len(x) - 1][1])
		return solution_matrix

def write_to_file(solution_matrix, output_file_name, max_time):
	c0 = round(solution_matrix[0][2], 6)
	c1 = round(solution_matrix[1][2], 6)
	if os.path.exists(output_file_name):
		os.remove(output_file_name)
	output_file = open(output_file_name, "a")
	output_file.write(f'0 <= x < {max_time}; y = {c0} + {c1}x; least-squares \n ')

def eliminate(A, src_row_idx, num_cols, num_rows):
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

def augment(x_transpose_x, x_transpose_y):
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

def gaussian(matrix):
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

def back_solve(matrix):
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

def print_result(matrix):
	column_count = len(matrix[0]) - 1
	vector = [0 for i in range(len(matrix))]
	for i in range(len(matrix)):
		vector[i] = matrix[i][column_count]
	result = "phi_hat = " + str(vector[0]) + " + " + str(vector[1]) + "x " + " + " + str(vector[2]) + "x^2"
	print(result)

def begin_run(X, Y):
	x_transpose = transpose(X)
	x_transpose_x = multiply(x_transpose, X)
	x_transpose_y = multiply(x_transpose, Y)
	x_transpose_x_x_transpose_y = augment(x_transpose_x, x_transpose_y)
	result = gaussian(x_transpose_x_x_transpose_y)
	rref = back_solve(result)
	print_result(rref)
