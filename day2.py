from util import get_input
import numpy as np

def condition1_satisfied(levels):
    return all_increasing(levels) or all_decreasing(levels)

def all_increasing(levels):
    arr = np.array(levels)
    diff = np.diff(arr)
    is_increasing = np.all(diff > 0)
    return is_increasing

def all_decreasing(levels):
    arr = np.array(levels)
    diff = np.diff(arr)
    is_decreasing = np.all(diff < 0)
    return is_decreasing

def condition2_satisfied(levels):
    arr = np.array(levels)
    diff = np.diff(arr)
    print(f"diff: {diff}")
    for d in diff:
        d = abs(d)
        if d < 1 or d > 3:
            return False
    
    return True


def main():
    # Input consists of many reports
    # One report per line
    # Each report is a list of numbers called levels, space deliminited
    input = get_input("2") 
    input = input.splitlines()
    # Part 1
    # Determine if a report is safe
    # Safe condition 1: The levels are ALL increasing or decreasing
    # Safe condition 2: Any two adjacent levels differ by AT LEAST ONE and AT MOST THREE
    # Return # of safe reports

    safe_count = 0
    for report in input:
        levels = report.split(" ")
        levels = [int(numeric_string) for numeric_string in levels]
        # print(f"{report}: {levels}")
        # print(f"Condition 1: {condition1_satisfied(levels)}")
        # print(f"Condition 2: {condition2_satisfied(levels)}")
        if condition1_satisfied(levels) and condition2_satisfied(levels):
            safe_count += 1
    
    print(f"safe count: {safe_count}")
  

if __name__ == "__main__":
    main()