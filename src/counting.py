#!/usr/bin/python3
#
#  counting.py
#
#  CLI interface for counting library
#
#

from argparse import ArgumentParser

from sys import argv as sysargv
from os import getenv

import logging

from counting_errors import InvalidCountingArgument

def main(height=1, width=1, steps=1, filename=None, autogenerate=False, points=None, verbocity=0, dryrun=False):
    """
    """
#    cell_obj = generate_cells(filename, autogenerate, points, verbose, dry-run)
    setup_logging(verbocity)
    return True

def setup_logging(verbocity):
    base_loglevel = getattr(logging, (getenv('LOGLEVEL', 'WARNING')).upper())
    verbocity = min(verbocity, 2)
    loglevel = base_loglevel - (verbocity * 10)
    logging.basicConfig(level=loglevel,
                        format='%(message)s')

def validate_args(**inargs):
    """
    Test and validate incoming arguments
    """
    if (inargs["height"] <= 0):
        raise InvalidCountingArgument(
                argname="height",
                argvalue=inargs["height"],
                message="Need a Height defined as greater than 0")
    if (inargs["width"] <= 0):
        raise InvalidCountingArgument(
                argname="width",
                argvalue=inargs["width"],
                message="Need a Width defined as greater than 0")
#    if (not(inargs["filename"]) and not(inargs["autogenerate"])):
#        return False
    if (inargs["steps"] <= 0):
        raise InvalidCountingArgument(
                argname="steps",
                argvalue=inargs["steps"],
                message="Need a Step Count defined as greater than 1")
    return inargs

def parse_args(*args, **kwargs):
    """
    """
    parser = ArgumentParser(
            prog="Counting",
            description="A CLI function to count the number of cells within a given distance of positive cells",
            epilog="")

    parser.add_argument('-f', '--filename',
            help="Name of the file that contains the stored cells")
    parser.add_argument('-a', '--autogenerate',
            help="Auto-generate a random array",
            default=False,
            action='store_true')
    parser.add_argument('-p', '--point',
            dest='points',
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
            help="(option) Output debug statements and verbose responses.  Repeat for increased verbocity.",
            dest='verbocity',
            default=0,
            action='count')
    parser.add_argument('-q', '--quiet',
            help="(option) Quiet, no verbosity, no unnecessary debug",
            action='store_const',
            const=-1,
            default=0,
            dest='verbocity')

    parser.add_argument('-D', '--dryrun',
            default=False,
            help="(option) Perform pre-flight operations, then quit before doing anything. [DEFAULT=False]",
            action='store_true')

    out_args = parser.parse_args(*args, **kwargs)
    out_vars = vars(out_args)
    return out_vars


if __name__ == "__main__":
#    main(validate_args(*parse_args(**sysargv[1:])))
    in_args = parse_args(*sysargv[1:])
    valid_args = validate_args(**in_args)
    main(**valid_args)




