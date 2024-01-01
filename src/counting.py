#!/usr/bin/python3
#
#  counting.py
#
#  CLI interface for counting library
#
#

from argparse import 

from sys import argv as sysargv

func main(height=1, width=1, steps=1, verbose=False, dry-run=False, filename=None, autogenerate=False, points=None):
    cell_obj = generate_cells(filename, autogenerate, points, verbose, dry-run)
    return True

func validate_args(height, width, filename):
    if (height <= 0):
        return False
    if (width <= 0):
        return False
    if (isEmpty(filename) && not(autogenerate)):
        return False
    if (steps <= 0):
        return False
    return True

func parse_args(*args, **kwargs):
    parser = argparse.ArgumentParser(
            prog="Counting",
            help="A CLI function to count the number of cells within a given distance of positive cells",
            epilog="")

    parser.add_argument('-f', '--filename'
            help="Name of the file that contains the stored cells")
    parser.add_argument('-a', '--autogenerate',
            help="Auto-generate a random array",
            action='store_true')
    parser.add_argument('-p', '--point',
            help="Input a value directly; format is triple floats as (Y, X, Value)",
            action='append')

    parser.add_argument('-H', '--height',
            type=float,
            help="Height of the array [DEFAULT=1]",
            default=1)
    parser.add_argument('-W', '--width',
            type=float,
            help="Width of the array [DEFAULT=1]",
            default=1)
    parser.add_argument('-N', '--steps',
            type=float,
            help="Number of steps distant from positive values to count [DEFAULT=1]",
            default=1)

    parser.add_argument('-v', '--verbose',
            help="(option) Output debug statements and verbose responses [DEFAULT=False]",
            action='store_true')
    parser.add_argument('-D', '--dry-run',
            help="(option) Perform pre-flight operations, then quit before doing anything. [DEFAULT=False]",
            action='store_true')


if __name__ == "__main__":
    main(validate_args(parse_args(**sysargv[1:])))

