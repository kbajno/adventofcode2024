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
    incorrectUpdates = []
    for page in individualPages:
        p = page.split(",")
        validPage = True
        for idx, num in enumerate(p):
            # verify the ordering is correct
            if num in rules.keys():
                rulesForNum = rules[num]
                # validate that no numbers in r come after the current index
                if all(x not in p[:idx] for x in rulesForNum) == False:
                    validPage = False
        
        if validPage:
            correctUpdates.append(p)
        else:
            incorrectUpdates.append(p)

    
    return correctUpdates, incorrectUpdates

def calculateMiddleValueTotal(validUpdates):
    total = 0

    for update in validUpdates:
        total += int(update[len(update)//2])

    return total

def checkIfOrderIsValid(rules, update):
    arr = []
    for idx, num in enumerate(update):
        if num in rules.keys():
            rulesForNum = rules[num]
            arr.append(all(x not in update[:idx] for x in rulesForNum))
        else:
            arr.append(True)
    return arr

def reorderIncorrectUpdates(rules, updates):
    ordered = []
    for u in updates:
        validityArr = checkIfOrderIsValid(rules, u)
        copy_u = u
        while(all(validityArr) == False):
            invalid_index = validityArr.index(False)
            # make it right
            num1 = copy_u[invalid_index-1]
            num2 = copy_u[invalid_index]
            copy_u[invalid_index-1] = num2
            copy_u[invalid_index] = num1
            validityArr = checkIfOrderIsValid(rules, copy_u)
        
        ordered.append(copy_u)
    return ordered

def main():
    input = get_input("5")
    splitInput = input.split("\n\n")
    rules = splitInput[0].strip()
    pages = splitInput[1].strip()

    dictRules = orderRules(rules)
    correctUpdates, incorrectUpdates = getCorrectUpdates(dictRules, pages)
    print(f"Correct updates total: {calculateMiddleValueTotal(correctUpdates)}")
    # re-order incorrect updates
    reorderedIncorrectUpdates = reorderIncorrectUpdates(dictRules, incorrectUpdates)
    # get middle total
    print(f"Incorrect updates total: {calculateMiddleValueTotal(reorderedIncorrectUpdates)}")

if __name__ == "__main__":
    main()