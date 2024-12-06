import unittest

from day5 import *

class OrderRulesTest(unittest.TestCase):

    rulesInput = """47|53
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

    pagesInput = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

    def test_orderRulesReturnsProperDict(self):
        expectedOutput = {
            "47": ["53", "13", "61", "29"],
            "97": ["13", "61", "47", "29", "53", "75"],
            "75": ["29", "53", "47", "61", "13"],
            "61": ["13","53","29"],
            "29": ["13"],
            "53": ["29", "13"]
        }

        actualOutput = orderRules(self.rulesInput)
        self.assertEqual(expectedOutput, actualOutput)

    def test_getCorrectUpdatesReturnsAccurateUpdates(self):
        rules = {
            "47": ["53", "13", "61", "29"],
            "97": ["13", "61", "47", "29", "53", "75"],
            "75": ["29", "53", "47", "61", "13"],
            "61": ["13","53","29"],
            "29": ["13"],
            "53": ["29", "13"]
        }
        
        expectedCorrectOutput = [['75', '47', '61', '53', '29'], ['97', '61', '53', '29', '13'], ['75', '29', '13']]
        expectedIncorrectOutput = [['75','97','47','61','53'], ['61','13','29'], ['97','13','75','29','47']]

        actualCorrectOutput, actualIncorrectOutput = getCorrectUpdates(rules, self.pagesInput)
        self.assertListEqual(expectedCorrectOutput, actualCorrectOutput)
        self.assertListEqual(expectedIncorrectOutput, actualIncorrectOutput)

    def test_reorderIncorrectUpdatesReturnsOrderedUpdates(self):
        input = [['75','97','47','61','53'], ['61','13','29'], ['97','13','75','29','47']]
        rules = {
            "47": ["53", "13", "61", "29"],
            "97": ["13", "61", "47", "29", "53", "75"],
            "75": ["29", "53", "47", "61", "13"],
            "61": ["13","53","29"],
            "29": ["13"],
            "53": ["29", "13"]
        }
        expectedOutput = [['97','75','47','61','53'], ['61','29','13'], ['97','75','47','29','13']]

        actualOutput = reorderIncorrectUpdates(rules, input)
        self.assertListEqual(expectedOutput, actualOutput)

    def test_calculateMiddleValueTotalReturnsCorrectTotal(self):
        validUpdates = [['75', '47', '61', '53', '29'], ['97', '61', '53', '29', '13'], ['75', '29', '13']]

        expectedOutput = 143

        actualOutput = calculateMiddleValueTotal(validUpdates)
        self.assertEqual(expectedOutput, actualOutput)

