# GMath
The old GMath Java library reworked and greatly improved. Some important functions still have to be added. GMath uses Python 3.6, so make sure you have that installed and use the 3.6 version of pip while installing.

## Install
To install, download the source and run:
```
$ pip install .
```
Pass `--upgrade` to upgrade.
If you want to edit GMath as you use it, install it by running:
```
$ pip install --editable .
```

## Usage
Example:
```
$ gmath fraction 0.08(3)
0.08(3) = 1/12
```
To get started, run:
```
$ gmath --help
```
To get more detailed help for a specific option, pass `--help` after the command:
```
$ gmath calcfunction --help
Usage: gmath calcfunction [OPTIONS] [POINTS]...

  Calculates the equation of a line or quadratic going through 2 or 3 given
  points.

Options:
  --help  Show this message and exit.
```
If you want to pass a negative number as an argument, by default GMath will think it is an option because it uses Click for the CLI. To fix this, type `--` and everything after will be parsed as an argument instead of an option.
Example:
```
$ gmath quadratic 5 -5 -360
Error: no such option: -5
$ gmath quadratic -- 5 -5 -360
5x^2 - 5x - 360 = 5(x - 9)(x + 8)
```
If you do this, make sure to enter any options before `--`.
Example:
```
$ gmath -o output.txt quadratic -- 5 -5 -360
```

## To do
* High degree polynomial factorization
* Dividing polynomials?
* Click is so slow, find a fix, probably a different CLI library
