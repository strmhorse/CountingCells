#!/usr/bin/python3
"""
cells_object.py

Object to hold and abstract details about the Cells object

"""

from collections import namedtuple, defaultdict

def constant_factory(value):
    return lambda: value

class Point = namedtuple('Point', ['y', 'x'], defaults=[0, 0])

class CellsObject:
    """
    """

    def __init__(self):
        """
        Create the default values dictionary.
        It uses the constant_factory to return 0 for any non-set value
        This simulates a sparse array
        """
        self._values = defaultdict(constant_factory(0))

    def validate_index(self, this_height, this_width):
        """
        Raises the InvalidIndexException if a value is beyond the set bounds.
        """
        if (this_height > self._height) or (this_width > self._width):
            raise InvalidIndexException(this_height, this_width, self._height, self._width)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, inval):
        if (inval <= 0):
            raise InvalidCountingArgument("height", inval)
        self._height = inval

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, inval):
        if (inval <= 0):
            raise InvalidCountingArgument("width", inval)
        self._width = inval

    @property
    def point(self, out_height, out_width):
        """
        Getter for point
        """
        self.validate_index(out_height, out_width)
        return self._values(Point(out_height, out_width))

    def set_point(self, in_height, in_width, in_value):
        """
        Setter for point
        TODO:  Value check the in_value
        """
        self.validate_index(in_height, in_width)
        self._values(Point(in_height, in_width)) = in_value

    point = property(set_point, get_point, del_point)



