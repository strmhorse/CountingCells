# countingpy/__init__.py

from countingpy.utils import *
from countingpy.counting_errors import *

def isBlank(inStr):
    """
    Used to test if a string is actually empty
    """
    return not (inStr and inStr.strip())

