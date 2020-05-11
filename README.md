# CPU Temperatures

This program takes CPU Temeratures as an input file and creates a piecewise
linear interpolation for each core and a global least squares approximation
for each core.

## Language
- [Python 3.7.4](https://www.python.org/downloads/release/python-374/)

## Requirments

- [Python 3.7.4](https://www.python.org/downloads/release/python-374/)
- [Typing Library](https://docs.python.org/3/library/typing.html)

## Compilation & Execution Instructions

### Installing

- You will need to install the libraries listed in the requirments section
before moving onto the execution instructions.

- If you do not already have it, install the typing library using the following command

```
pip3 install typing
```

### Execution Instructions

- Open the terminal on Mac, Linux or Bash on Windows and cd to the root of the project
- Give the following command to run the program

```
python3 begin_run.py sensors-2018.12.26-no-labels.txt no
```

#### Command Format:

```
python3 begin_run.py input_file_name.txt has_labels?
```

#### Errors:

If you are having compilation errors, here are some of the possible issues:
1. Make sure you are using python 3 or higher
2. Make sure that the input file you give is in the input directory and
  when passing the file name as a command line argument only give the file name and extension,
 do not  give a path

## Documentation

The documentation for this project is generated using [Pydoc](https://docs.python.org/3/library/pydoc.html).
Html output is genrated and can be found in `CPU-Temperatures/docs/` directory. You can also view the documentation
for a python file by giving the following command

```
pydoc3.7 utils
```
This will show to documentation for the utils file, you can change that to any python file to view the documentation or you
can view the html output for the given file in the docs directory

You can also generate an html output for a file by giving the following command

```
pydoc3.7 -w utils
```
This will generate an html page for the utils.py file in the current directory

## Table of Contents

- [Matrix Solver](https://github.com/AbelWeldaregay/CPU-Temperatures/tree/master/matrix_solver)


