# GMath
The old GMath Java library reworked and greatly improved. Some important functions still have to be added.

## Install
To install, download the source and run:
```
$ pip install .
```
Pass `--upgrade` to upgrade.

## Usage
To get started, run:
```
$ gmath --help
```
Example:
```
$ gmath fraction 0.08(3)
0.08(3) = 1/12
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

## To do
* Add ability to recognize and calculate equations of arithmetic, geometric, and quadratic sequences
* Change command line programming to click
