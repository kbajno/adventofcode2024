import numpy as np
from util import get_input

# Return: dict where key is the num, and val is array of numbers key must come before
def orderRules(rules):
    orderedRules = {}
    splitRules = rules.strip().split("\n")
    for rule in splitRules:
        nums = rule.split("|")
        numBefore = nums[0]
        numAfter = nums[1]
        if numBefore in orderedRules.keys():
            orderedRules[numBefore].append(numAfter)
        else:
            orderedRules[numBefore] = [numAfter]
    return orderedRules

def getCorrectUpdates(rules, pages):
    individualPages = pages.strip().split("\n")

    correctUpdates = []
    for page in individualPages:
        p = page.split(",")
        validPage = True
        for idx, num in enumerate(p):
            # verify the ordering is correct
            if num in rules.keys():
                rulesForNum = rules[num]
                # print(f"number {num}, must come before {rules[num]}")
                # validate that no numbers in r come after the current index
                # print(f"valid ordering: {all(x not in p[:idx] for x in rulesForNum)}")
                if all(x not in p[:idx] for x in rulesForNum) == False:
                    validPage = False
        
        if validPage:
            # print(f"VALID PAGE: {p}")
            correctUpdates.append(p)

    
    return correctUpdates

def main():
    input = get_input("5")
    splitInput = input.split("\n\n")
    rules = splitInput[0].strip()
    pages = splitInput[1].strip()

    dictRules = orderRules(rules)
    # print(dictRules)
    updates = getCorrectUpdates(dictRules, pages)
    # print(updates)

if __name__ == "__main__":
    main()