#!/usr/bin/python3
"""
counting.py

The CLI wrapper for the counting project.

"""

#__package__ = "countingpy"

from argparse import ArgumentParser

from sys import argv as sysargv, exit as sysexit
from os import getenv

import logging
import pprint

import utils as counting_utils
#import countingpy.utils as counting_utils
#from ..utils import isBlank, setupLogging
#from utils import isBlank, setupLogging

from counting_errors import InvalidCountingArgument
#from countingpy.counting_errors import InvalidCountingArgument

from generate_cells import generate_cells_obj


def main(filename=None, steps=0, verbocity=0, **kwargs):
    """
    Main runner for the counting functions
    """
    cell_obj = generate_cells_obj(filename=filename)
    return cell_obj.count(steps)
#    setupLogging(verbocity)


def validate_args(**inargs):
    """
    Test and validate incoming arguments
    """
    if inargs["height"] <= 0:
        raise InvalidCountingArgument("height", inargs["height"])
    if inargs["width"] <= 0:
        raise InvalidCountingArgument("width", inargs["width"])
#    if isBlank(inargs["filename"]):
#        logging.debug("File is blank")
#    if (not(inargs["filename"]) and not(inargs["autogenerate"])):
#        return False
    if inargs["steps"] < 0:
        raise InvalidCountingArgument("step", inargs["steps"])
    if inargs["verbocity"]:
        print("\n\n\nVerbose Output of command line arguments:")
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(inargs)
        print("\n\n")

    if inargs["dryrun"]:
        print("Dry Run, exiting...\n\n")
        sysexit(0)

    return inargs

def parse_args(*args, **kwargs):
    """
    Parses incoming arguments into usable variables.
    """
    parser = ArgumentParser(
            prog="Counting",
            description="A CLI function to count the number of cells within "
                        "a given distance of positive cells",
            epilog="\n\n\n")

    parser.set_defaults(
            filename=None,
            verbocity=0
            )

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

    source_group = parser.add_argument_group(
            title="Source Group",
            description="Where are the cell values coming from?")
    source_group.add_argument('-f', '--filename',
            help="Name of the file that contains the stored cells",
            default=None)
    source_group.add_argument('-a', '--autogenerate',
            help="Auto-generate a random array [DEFAULT=False]",
            default=False,
            action='store_true')
    source_group.add_argument('-p', '--point',
            dest='points',
            help="(option) Input a value directly; format is triple floats as (Y, X, Value)",
            action='append')


    helper_group = parser.add_argument_group(title='helpers',
            description="These are helper functions, not related to the main system operation.")
    helper_group.add_argument('-D', '--dryrun',
            default=False,
            help="(option) Perform pre-flight operations, then quit before "
                 "doing anything. [DEFAULT=False]",
            action='store_true')
    verb_group = helper_group.add_mutually_exclusive_group(required=False)
    verb_group.add_argument('-v', '--verbose',
            help="(option) Output debug statements and verbose responses.  "
                 "Repeat for increased verbocity.",
            dest='verbocity',
            default=0,
            action='count')
    verb_group.add_argument('-q', '--quiet',
            help="(option) Quiet, no verbocity, no unnecessary debug",
            action='store_const',
            const=-1,
            default=0,
            dest='verbocity')

    out_args = parser.parse_args(*args, **kwargs)
    out_vars = vars(out_args)
    return out_vars


if __name__ == "__main__":
#    main(validate_args(*parse_args(**sysargv[1:])))
    in_args = parse_args(sysargv[1:])
    valid_args = validate_args(**in_args)
    cval = main(**valid_args)
    print(f"\n\n\nCount is {cval}")
