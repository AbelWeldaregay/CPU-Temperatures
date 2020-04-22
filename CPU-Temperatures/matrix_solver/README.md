# Matrix Solver

## Language
- Python 3.7.4

# Pseudocode
### Gaussian Elimination
Let A be an n by n matrix with an augmented vector in col n
```
Iterate through all rows
for every i in 0 to n-1:
    # Pick a pivot
    max_idx = find_largest_row_by_col(A, col_index, num_rows)
    swap_row(A, i, max_idx)
    
    scale(A, i, num_cols, A[i][i])
    A[i][i] = 1

    eliminate(A, i, num_rows)

```
### Scale

```
def scale_row(A, row_idx, num_cols, s):

    for every j in 0 to num_cols:
        A[row_idx][j] = A[row_idx][j] / s
```

### Eliminate

```
def eliminate(A, src_row_idx, num_cols, num_rows):

    start_col <- src_row_idx

    for every i in (src_row_idx + 1) to num_rows:

        s <- A[i][start_col]

        for every j in start_col to num_cols:
            A[i][j] = A[i][j] - s * A[src_row_idx][j]

        A[i][start_col] = 0

```
### Backsolve
```
def back_solve(matrix):

    augColIdx <- matrix.cols()  # the augmented column
    lastRow = matrix.rows() - 1

    for i in lastRow down to 1:
        for j <- (i - 1) down to 0:
            s <- matrix[j][i]

            matrix[j][i] -= (s * matrix[i][i])
            matrix[j][augCol] -= (s * matrix[i][augColIdx])
```

## Requirements

[Python 3.7.4](https://www.python.org/downloads/release/python-374/)


## Compilation & Execution Instructions

### Installing
- Open the terminal on Mac, Linux or Bash on Windows
- Give the following commands to initialize a git repository and clone the project

```
git init .
```

```
git clone https://github.com/AbelWeldaregay/Computational-Methods-and-Software.git
```

### Running

After you are in `/Computational-Methods-and-Software/machine_assignments/machine_assignment_3` directory, give the following command to run the script:

```
python matrix_solver.py
```
