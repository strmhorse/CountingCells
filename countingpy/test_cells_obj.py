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
        self.assertEqual(co1.get_point(1, 1), 0)

    def test_set_init(self):
        """
        Test setting an object at initialization
        """
        co2 = CellsObject(height=3, width=3, values=in_dict_1)
        self.assertEqual(co2.height, 3)
        self.assertEqual(co2.width, 3)
        self.assertEqual(co2.get_point(1, 1), in_dict_1[Point(1,1)])
        self.assertEqual(co2.get_point(1, 3), in_dict_1[Point(1,3)])
        self.assertEqual(co2.get_point(3, 1), in_dict_1[Point(3,1)])
        self.assertEqual(co2.get_point(3, 3), in_dict_1[Point(3,3)])
        self.assertEqual(co2._values, in_dict_1)

    def test_maximums(self):
        """
        Test setting an object at initialization
        """
        co3 = CellsObject(values=in_dict_1)
        self.assertEqual(co3.height, 3)
        self.assertEqual(co3.width, 3)
        self.assertEqual(co3.get_point(1, 1), in_dict_1[Point(1,1)])
        self.assertEqual(co3.get_point(1, 3), in_dict_1[Point(1,3)])
        self.assertEqual(co3.get_point(3, 1), in_dict_1[Point(3,1)])
        self.assertEqual(co3.get_point(3, 3), in_dict_1[Point(3,3)])
        self.assertEqual(co3._values, in_dict_1)

    def test_setters(self):
        """
        Test setting object values through getter's and setter's
        """
        co4 = CellsObject()
        co4.height = 3
        self.assertEqual(co4.height, 3)
        co4.width = 3
        self.assertEqual(co4.width, 3)
        for ((y,x), val) in in_dict_1.items():
            co4.set_point(y, x, val)
        self.assertEqual(co4.get_point(1, 1), in_dict_1[Point(1,1)])
        self.assertEqual(co4.get_point(1, 3), in_dict_1[Point(1,3)])
        self.assertEqual(co4.get_point(3, 1), in_dict_1[Point(3,1)])
        self.assertEqual(co4.get_point(3, 3), in_dict_1[Point(3,3)])
        self.assertEqual(co4._values, in_dict_1)

    def test_set_index_bad_index(self):
        """
        Test bounds checking on setters
        """
        co5 = CellsObject(values=in_dict_1)
        with self.assertRaises(InvalidCountingArgument):
            co5.height = 0
        self.assertEqual(co5.height, 3)
        with self.assertRaises(InvalidCountingArgument):
            co5.width = 0
        self.assertEqual(co5.width, 3)

    def test_getter_bad_index(self):
        """
        Test bounds checking on getters
        """
        co6 = CellsObject(values=in_dict_1)
        with self.assertRaises(InvalidIndexException):
            co6.get_point(4,1)
        with self.assertRaises(InvalidIndexException):
            co6.get_point(1,4)
        with self.assertRaises(InvalidIndexException):
            co6.get_point(4,4)
        with self.assertRaises(InvalidIndexException):
            co6.get_point(-1, -1)

    def test_setter_bad_index(self):
        """
        Test bounds checking on setters
        """
        co7 = CellsObject(values=in_dict_1)
        with self.assertRaises(InvalidIndexException):
            co7.set_point(4, 1, 1)
        with self.assertRaises(InvalidIndexException):
            co7.set_point(1, 4, 1)
        with self.assertRaises(InvalidIndexException):
            co7.set_point(4, 4, 1)
        with self.assertRaises(InvalidIndexException):
            co7.set_point(-1, -1, 1)

    def test_setter_bad_value(self):
        """
        Test bounds checking on setters
        """
        co8 = CellsObject(values=in_dict_1)
        with self.assertRaises(InvalidValueException):
            co8.set_point(1, 1, "-1")
        with self.assertRaises(InvalidValueException):
            co8.set_point(1, 1, "Shaggy")

    def test_odd_sizes(self):
        """
        Compare to a 9x9 array
        """
        co9 = CellsObject(values=in_dict_2)
        self.assertEqual(co9.height, 9)
        self.assertEqual(co9.width, 9)
        self.assertEqual(co9._values, in_dict_2)


    def test_odd_sizes2(self):
        """
        Compare to a 1x11 array
        """
        co10 = CellsObject(values=in_dict_3)
        self.assertEqual(co10.height, 1)
        self.assertEqual(co10.width, 11)
        self.assertEqual(co10._values, in_dict_3)

    def test_odd_sizes_4(self):
        """
        Compare to a 11x1 array
        """
        co11 = CellsObject(values=in_dict_4)
        self.assertEqual(co11.height, 11)
        self.assertEqual(co11.width, 1)
        self.assertEqual(co11._values, in_dict_4)

    def test_odd_sizes_5(self):
        """
        Compare to a 1x1 array
        """
        co12 = CellsObject(values=in_dict_5)
        self.assertEqual(co12.height, 1)
        self.assertEqual(co12.width, 1)
        self.assertEqual(co12._values, in_dict_5)

    def test_positives(self):
        """
        Compare positives
        """
        co13 = CellsObject(values=in_dict_1)
        self.assertEqual(co13._positives, positives_1)

    def test_distance_1(self):
        """
        Test the distance functions
        """
        co14 = CellsObject(values=in_dict_2)
        self.assertEqual(co14.distance(1,1,1,1), 0)
        self.assertEqual(co14.distance(2,1,1,1), 1)
        self.assertEqual(co14.distance(1,2,1,1), 1)
        self.assertEqual(co14.distance(1,1,2,1), 1)
        self.assertEqual(co14.distance(1,1,1,2), 1)
        self.assertEqual(co14.distance(1,1,9,9), 16)
        self.assertEqual(co14.distance(9,9,1,1), 16)
        self.assertEqual(co14.distance(9,1,1,9), 16)
        self.assertEqual(co14.distance(1,9,9,1), 16)

    def test_distance_2(self):
        """
        Test the distance functions
        """
        co14 = CellsObject(values=in_dict_2)
        self.assertEqual(co14.distance(p1=Point(1,1),p2=Point(1,1)), 0)
        self.assertEqual(co14.distance(p1=Point(2,1),p2=Point(1,1)), 1)
        self.assertEqual(co14.distance(p1=Point(1,2),p2=Point(1,1)), 1)
        self.assertEqual(co14.distance(p1=Point(1,1),p2=Point(2,1)), 1)
        self.assertEqual(co14.distance(p1=Point(1,1),p2=Point(1,2)), 1)
        self.assertEqual(co14.distance(p1=Point(1,1),p2=Point(9,9)), 16)
        self.assertEqual(co14.distance(p1=Point(9,9),p2=Point(1,1)), 16)
        self.assertEqual(co14.distance(p1=Point(9,1),p2=Point(1,9)), 16)
        self.assertEqual(co14.distance(p1=Point(1,9),p2=Point(9,1)), 16)

    def test_neighborhood_1(self):
        """
        Test the neighborhood function
        """
        co15 = CellsObject(values=in_dict_1)
        p_val_1 = co15.neighborhood_of_positives(1)
        self.assertEqual(p_val_1, positives_1.keys())
        p_val_2 = co15.neighborhood_of_positives(2)
        self.assertEqual(p_val_2, positives_1.keys())





# Test Del
# Test Positives
# Test Distance

in_dict_1 = {
    Point(1,1): 0,
    Point(1,2): 2,
    Point(1,3): 4,
    Point(2,1): -2,
    Point(2,2): -4,
    Point(2,3): -6,
    Point(3,1): -1,
    Point(3,2): -3,
    Point(3,3): 5
}

positives_1 = {
    Point(1,2): 2,
    Point(1,3): 4,
    Point(3,3): 5
}

positives_2 = {
    Point(1,1): 0,
    Point(1,2): 2,
    Point(1,3): 4,
    Point(2,1): -2,
    Point(2,3): -6,
    Point(3,2): -3,
    Point(3,3): 5
}

def generate_dict(y=1, x=1):
    """
    NOTE:  Indexes are 1 to n+1 due to python range weirdness.
    Starts at 0, ends at n-1.
    """
    outdict = {}
    for x_val in range(1, x+1):
        for y_val in range(1, y+1):
            modval = ((y_val + x_val) % 3) -1
            outdict[Point(y_val, x_val)] = modval
    return outdict

in_dict_2 = generate_dict(9, 9)
in_dict_3 = generate_dict(1, 11)
in_dict_4 = generate_dict(11, 1)
in_dict_5 = generate_dict(1, 1)
#
