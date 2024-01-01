#!/usr/bin/python3
"""
cells_object.py

Object to hold and abstract details about the Cells object

"""

from collections import namedtuple
#from collections import defaultdict
from numbers import Number

from counting_errors import InvalidIndexException, InvalidCountingArgument, InvalidValueException

#def constant_factory(value):
#    """
#    Just a default return function
#    """
#    return lambda: value

Point = namedtuple('Point', ['y', 'x'], defaults=[0, 0])

#class Point(namedtuple('Point', ['y', 'x'], defaults=[0,0])):
#    __slots__ = ()
#    def __str__

class CellsObject:
    """
    Object to hold and return the value of cells in an array
    """

    def __init__(self, height=1, width=1, values=None, default_value=0):
        """
        Create the default values dictionary.
        It uses the constant_factory to return 0 for any non-set value
        This simulates a sparse array
        """
        self._height = height
        self._width = width
        self._default_value = default_value
        #self._values = defaultdict(constant_factory(0))
        self._values = values or {}

    def validate_index(self, height, width):
        """
        Tests the given index values against the expected index values.
        Raises the InvalidIndexException if a value is beyond the set bounds.
        """
        if (height > self._height) or (height < 0) or (width > self._width) or (width < 0):
            raise InvalidIndexException(height, width, self._height, self._width)

    def validate_value(self, in_value):
        """
        Tests the given value for proper type
        """
        if not isinstance(in_value, Number):
            raise InvalidValueException(in_value)


    @property
    def height(self):
        """
        Gets the height index limit of the array
        Raises an exception if the index is invalid.
        """
        return self._height

    @height.setter
    def height(self, inval):
        """
        Sets the height index limit of the array
        Raises an exception if the index is invalid.
        """
        if inval <= 0:
            raise InvalidCountingArgument("height", inval)
        self._height = inval

    @property
    def width(self):
        """
        Gets the width index limit of the array
        Raises an exception if the index is invalid.
        """
        return self._width

    @width.setter
    def width(self, inval):
        """
        Sets the width index limit of the array
        Raises an exception if the index is invalid.
        """
        if inval <= 0:
            raise InvalidCountingArgument("width", inval)
        self._width = inval

    def get_point(self, out_height, out_width):
        """
        Gets the value of any point in the array.
        Returns the default value if no value has been set.
        Raises an exception if the index is invalid.
        """
        self.validate_index(out_height, out_width)
        try:
            return self._values[Point(out_height, out_width)]
        except KeyError:
            return self._default_value

    def set_point(self, in_height, in_width, in_value):
        """
        Sets the point value in the array.
        Raises an exception if either the index or value are invalid.
        """
        self.validate_index(in_height, in_width)
        self.validate_value(in_value)
        index = Point(in_height, in_width)
        self._values[index] = in_value

    def del_point(self, in_height, in_width):
        """
        Gets the value of any point in the array
        Raises an exception if the index is invalid.
        """
        self.validate_index(in_height, in_width)
        self._values.pop([Point(in_height, in_width)], None)
#
