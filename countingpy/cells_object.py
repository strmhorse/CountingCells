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

    def __init__(self, height=1, width=1, values=None, default_value=0, verbocity=0):
        """
        Create the default values dictionary.
        It uses the constant_factory to return 0 for any non-set value
        This simulates a sparse array
        """
        self._height = height
        self._width = width
        self._default_value = default_value
        self._verbocity = verbocity
        #self._values = defaultdict(constant_factory(0))
        self._values = values or {}
        self._positives = {}
        self.generate_positives()
        self.generate_maximums()

    def reset_maximums(self, y, x):
        """
        Re-sets the maximums from a given indexes
        """
        changed = False
        if y > self._height:
            self.height = y
            changed = True
        if x > self._width:
            self._width = x
            changed = True
        if changed and self._verbocity:
            print(f"Maximum Indexes are now:  {self._height}, {self._width}")

    def generate_maximums(self):
        """
        Re-sets the maximums from the incoming values array
        """
        for ((y, x)) in self._values.keys():
            self.reset_maximums(y, x)
#        if changed:
#            print(f"Values are now:  {self._height}, {self._width}")

    def generate_positives(self):
        """
        Initialize the positives array
        """
        for ((y, x), val) in self._values.items():
            if val > 0:
                self._positives[Point(y, x)] = val

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
#        self.validate_index(in_height, in_width)
        self.reset_maximums(in_height, in_width)
        self.validate_value(in_value)
        self._values[Point(in_height, in_width)] = in_value
        self.set_positive(in_height, in_width, in_value)

    def del_point(self, in_height, in_width):
        """
        Gets the value of any point in the array
        Raises an exception if the index is invalid.
        """
        self.validate_index(in_height, in_width)
        try:
            self._values.pop([Point(in_height, in_width)], None)
        except KeyError:
            pass
        self.del_positive(in_height, in_width)

    def get_positive(self, out_height, out_width):
        """
        Gets the value of any point in the array.
        Returns the default value if no value has been set.
        Raises an exception if the index is invalid.
        """
        self.validate_index(out_height, out_width)
        try:
            return self._positives[Point(out_height, out_width)]
        except KeyError:
            return False

    def set_positive(self, in_height, in_width, in_value):
        """
        Sets the point value in the array.
        Raises an exception if either the index or value are invalid.
        """
        self.validate_index(in_height, in_width)
        if in_value > 0:
            self._positives[Point(in_height, in_width)] = True

    def del_positive(self, in_height, in_width):
        """
        Gets the value of any point in the array
        Raises an exception if the index is invalid.
        """
        self.validate_index(in_height, in_width)
        try:
            self._positives.pop([Point(in_height, in_width)], None)
        except KeyError:
            pass

    def distance(self, y1=0, x1=0, y2=0, x2=0, p1=None, p2=None):
        """
        This is the implementation of the Manhattan Distance formula
        """
        p1 = p1 or Point(y1, x1)
        p2 = p2 or Point(y2, x2)
        self.validate_index(p1.y, p1.x)
        self.validate_index(p2.y, p2.x)
        d = abs(p1.y - p2.y) + abs(p1.x - p2.x)
        return d

    def neighborhood_of_positives(self, steps=1):
        """
        Find how many cells are in the neighborhood of positive integers
        """
        found_list = []
        for point_index_v in self._values.keys():
            for point_index_p in self._positives.keys():
                if self.distance(p1=point_index_v, p2=point_index_p) <= steps:
                    found_list.append(point_index_v)
        found_set = set(found_list)
        return found_set

    def count(self, steps=1):
        """
        Return the count for the number of unique cells within steps of positives
        """
        countval = len(self.neighborhood_of_positives(steps))
        if self._verbocity:
            print(f"Count Value is {countval}\n\n")
        return countval





#
