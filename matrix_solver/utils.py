import sys

def multiply(A, B):
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
	result = [[0 for i in range(len(B[0]))] for j in range(len(A))]
	
	for i in range(len(result)):
		for j in range(len(result[0])):
			for k in range(len(A[0])):
				result[i][j] += A[i][k]*B[k][j]
	return result

def compute_x(A):
	"""
	Builds the X matrix using the algorithm from the lecture notes
	1. The first column is defined by taking each x value and plugging it into y=1.
	2. The second column is defined by taking each x value and plugging it into y=x. 2
	3. The third column is defined by taking each x value and plugging it into y=x2.
	"""
	result = [[0 for i in range(2)] for j in range(len(A))]
	for i in range(len(result)):
		result[i][0] = 1
		result[i][1] = A[i][0]
	return result

def compute_y(A):
	"""
	Builds the Y matrix using the algorithm from the lecture notes
	"""
	result = [0 for i in range(len(A))]
	for i in range(len(result)):
		result[i] = A[i][1]
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
	result = [[0 for i in range(len(A))] for j in range(len(A[0]))]
	for i in range(len(A[0])):
		for j in range(len(A)):
			result[i][j] = A[j][i]
	return result

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
