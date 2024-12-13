import unittest

from day6 import *

class Day6Test(unittest.TestCase):

    map = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    # def test_orderRulesReturnsProperDict(self):
    #     expectedOutput = {
    #         "47": ["53", "13", "61", "29"],
    #         "97": ["13", "61", "47", "29", "53", "75"],
    #         "75": ["29", "53", "47", "61", "13"],
    #         "61": ["13","53","29"],
    #         "29": ["13"],
    #         "53": ["29", "13"]
    #     }

    #     actualOutput = orderRules(self.rulesInput)
    #     self.assertEqual(expectedOutput, actualOutput)