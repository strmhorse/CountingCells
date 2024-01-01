#!/usr/bin/python3
"""
test_counting.py

Testing for the validation of arguments.
"""

import unittest

from counting import validate_args
#from countingpy.counting import validateArgs

from counting_errors import InvalidCountingArgument

testDictGood = {
        "height": 1,
        "width": 1,
        "steps": 1,
        "verbocity" :0,
        "dryrun": False
        }



class TestValidateArguments(unittest.TestCase):
    """
    Testing the Validate Arguments function.
    """
    def test_height_good(self):
        """
        This is a default validation for known good values.
        """
        return_dict = validate_args(**testDictGood)
        self.assertEqual(return_dict, testDictGood)

    def test_height_bad(self):
        """
        Boundry testing for height > 0
        """
        bad_input_dict = testDictGood.copy()
        bad_input_dict["height"] = 0
        with self.assertRaises(InvalidCountingArgument):
            validate_args(**bad_input_dict)
        bad_input_dict["height"] = -1
        with self.assertRaises(InvalidCountingArgument):
            validate_args(**bad_input_dict)

    def test_width_bad(self):
        """
        Boundry testing for width > 0
        """
        bad_input_dict = testDictGood.copy()
        bad_input_dict["width"] = 0
        with self.assertRaises(InvalidCountingArgument):
            validate_args(**bad_input_dict)
        bad_input_dict["width"] = -1
        with self.assertRaises(InvalidCountingArgument):
            validate_args(**bad_input_dict)

    def test_step_bad(self):
        """
        Boundry testing for step > 0
        """
        bad_input_dict = testDictGood.copy()
        bad_input_dict["steps"] = 0
        with self.assertRaises(InvalidCountingArgument):
            validate_args(**bad_input_dict)
        bad_input_dict["steps"] = -1
        with self.assertRaises(InvalidCountingArgument):
            validate_args(**bad_input_dict)


if __name__ == "__main__":
    unittest.main()
