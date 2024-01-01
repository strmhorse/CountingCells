#!/usr/bin/python3

import unittest

from counting import validateArgs

testDictGood = {
        "height": 1,
        "width": 1,
        "steps": 1,
        "verbocity" :1
        }



class TestValidateArguments(unittest.TestCase):
    def test_height_bad(self):
        badDict = testDictGood.copy()
        badDict["height"] = 0
        with self.assertRaises(InvalidCountingArgument):
            validateArgs(badDict)


if __name__ == "__main__":
    unittest.main()
