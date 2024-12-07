from util import get_input

def addAll(nums):
    op = ('+').join(nums)
    return eval(op)

def multAll(nums):
    op = ('*').join(nums)
    return eval(op)

def compare(num1, num2):
    return int(num1) == int(num2)

def main():
    # input = get_input("7")
    input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

    nums = {}
    lines = input.splitlines()
    for line in lines:
        l = line.split(':')
        total = l[0]
        n = l[1].strip().split(' ')
        nums[total] = n

    operands = ['+', '*']
    true_vals = []

    for i in nums:
        print(f'Evaluating {i}: {nums[i]}')
        # try all +
        test_val = i
        sum = addAll(nums[i])
        print(f'test_val: {test_val} sum: {sum}')

        if compare(test_val,  sum):
            true_vals.append(test_val)

        # try all *
        test_val = i
        sum = multAll(nums[i])
        print(f'test_val: {test_val} sum: {sum}')

        if compare(test_val,  sum):
            true_vals.append(test_val)

        # total_combinations = ((len(nums[n])-1) * (len(operands)))

    total = 0
    for val in true_vals:
        total += int(val)
    print(f'total calibration result: {total}')
if __name__ == "__main__":
    main()