#!/usr/bin/python3
"""
test_cells_obj.py

Test for the Cells object
"""

import unittest

from cells_object import Point
from cells_object import CellsObject

from counting_errors import InvalidCountingArgument, InvalidIndexException, InvalidValueException

class TestPoint(unittest.TestCase):
    """
    Tester for the Point class of namedtuple
    """
    def test_default(self):
        """
        Test an empty point
        """
        p1 = Point()
        self.assertEqual(p1.y, 0)
        self.assertEqual(p1.x, 0)
        self.assertEqual(p1, (0,0))

    def test_value(self):
        """
        Test a non-empty point
        """
        p2 = Point(3, 5)
        self.assertEqual(p2.y, 3)
        self.assertEqual(p2.x, 5)
        self.assertEqual(p2, (3, 5))

class TestCellsObject(unittest.TestCase):
    """
    Tester for the CellsObject Class
    """
    def test_default(self):
        """
        Test an uninitialized object
        """
        co1 = CellsObject()
        self.assertEqual(co1.height, 1)
        self.assertEqual(co1.width, 1)
        self.assertEqual(co1.get_point(0, 0), 0)

    def test_set_init(self):
        """
        Test setting an object at initialization
        """
        co2 = CellsObject(height=3, width=3, values=in_dict_1)
        self.assertEqual(co2.height, 3)
        self.assertEqual(co2.width, 3)
        self.assertEqual(co2.get_point(0, 0), 0)
        self.assertEqual(co2.get_point(1, 2), 4)
        self.assertEqual(co2.get_point(2, 2), -4)
        self.assertEqual(co2._values, in_dict_1)

    def test_setters(self):
        """
        Test setting object values through getter's and setter's
        """
        co3 = CellsObject()
        co3.height = 3
        self.assertEqual(co3.height, 3)
        co3.width = 3
        self.assertEqual(co3.width, 3)
        for ((y,x), val) in in_dict_1.items():
            co3.set_point(y, x, val)
        self.assertEqual(co3.get_point(0, 0), 0)
        self.assertEqual(co3.get_point(1, 2), 4)
        self.assertEqual(co3.get_point(2, 2), -4)
        self.assertEqual(co3._values, in_dict_1)

    def test_set_index_bad_index(self):
        """
        Test bounds checking on setters
        """
        co4 = CellsObject(height=3, width=3, values=in_dict_1)
        with self.assertRaises(InvalidCountingArgument):
            co4.height = 0
        self.assertEqual(co4.height, 3)
        with self.assertRaises(InvalidCountingArgument):
            co4.width = 0
        self.assertEqual(co4.width, 3)

    def test_getter_bad_index(self):
        """
        Test bounds checking on getters
        """
        co5 = CellsObject(height=3, width=3, values=in_dict_1)
        with self.assertRaises(InvalidIndexException):
            co5.get_point(4,1)
        with self.assertRaises(InvalidIndexException):
            co5.get_point(1,4)
        with self.assertRaises(InvalidIndexException):
            co5.get_point(4,4)
        with self.assertRaises(InvalidIndexException):
            co5.get_point(-1, -1)

    def test_setter_bad_index(self):
        """
        Test bounds checking on setters
        """
        co6 = CellsObject(height=3, width=3, values=in_dict_1)
        with self.assertRaises(InvalidIndexException):
            co6.set_point(4, 1, 1)
        with self.assertRaises(InvalidIndexException):
            co6.set_point(1, 4, 1)
        with self.assertRaises(InvalidIndexException):
            co6.set_point(4, 4, 1)
        with self.assertRaises(InvalidIndexException):
            co6.set_point(-1, -1, 1)

    def test_setter_bad_value(self):
        """
        Test bounds checking on setters
        """
        co6 = CellsObject(height=3, width=3, values=in_dict_1)
        with self.assertRaises(InvalidValueException):
            co6.set_point(1, 1, "-1")
        with self.assertRaises(InvalidValueException):
            co6.set_point(1, 1, "Shaggy")




in_dict_1 = {
    Point(0,0): 0,
    Point(0,1): 1,
    Point(0,2): 2,
    Point(1,0): 0,
    Point(1,1): 2,
    Point(1,2): 4,
    Point(2,0): 0,
    Point(2,1): -2,
    Point(2,2): -4
}
#
