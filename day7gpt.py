from itertools import product
from util import get_input

def evaluate_expression(numbers, operators):
    """
    Evaluate the expression with the given numbers and operators in left-to-right order.
    """
    result = numbers[0]  # Start with the first number
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
        elif operator == '||':
            print(result)
            print(f'num 1 {numbers[i]} num 2 {numbers[i+1]}')
            result = int(str(numbers[i]) + str(numbers[i+1]))
            print(result)
    return result

def find_valid_equations(lines):
    total_calibration_result = 0
    for line in lines:
        # Parse the input line
        target, values = line.split(": ")
        target = int(target)
        numbers = list(map(int, values.split()))
        
        # Generate all possible operator combinations ("+" or "*")
        num_slots = len(numbers) - 1
        operator_combinations = product(['+', '*', '||'], repeat=num_slots)
        # Check all combinations
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == target:
                total_calibration_result += target
                break  # No need to check further combinations for this line
                
    return total_calibration_result

def main():
    input_data = get_input("7")
    lines = input_data.strip().split('\n')
    result = find_valid_equations(lines)
    print("Total Calibration Result:", result)

if __name__ == "__main__":
    main()
