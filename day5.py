from util import get_input

def orderRules(rules):
    orderedRules = {}
    splitRules = rules.split("\n")
    for rule in splitRules:
        nums = rule.split("|")
        numBefore = nums[0]
        numAfter = nums[1]
        if numBefore in orderedRules.keys():
            orderedRules[numBefore].append(numAfter)
        else:
            orderedRules[numBefore] = [numAfter]
    return orderedRules

def main():
    input = get_input("5")
    splitInput = input.split("\n\n")
    rules = splitInput[0].rstrip()
    pages = splitInput[1].rstrip()

    dictRules = orderRules(rules)
    print(dictRules)
if __name__ == "__main__":
    main()