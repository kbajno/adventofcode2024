import unittest

from day5 import orderRules

class OrderRulesTest(unittest.TestCase):

    def test_orderRulesReturnsProperDict(self):
        input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

        expectedOutput = {
            "47": ["53", "13", "61", "29"],
            "97": ["13", "61", "47", "29", "53", "75"],
            "75": ["29", "53", "47", "61", "13"],
            "61": ["13","53","29"],
            "29": ["13"],
            "53": ["29", "13"]
        }

        actualOutput = orderRules(input)
        self.assertEqual(expectedOutput, actualOutput)


