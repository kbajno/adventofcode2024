from util import get_input

def addAll(nums):
    op = ('+').join(nums)
    return eval(op)

def multAll(nums):
    op = ('*').join(nums)
    return eval(op)

def compare(num1, num2):
    return int(num1) == int(num2)

def evalOps(nums, op):
    cmd = [nums[0]]
    for idx, o in enumerate(op):
        cmd.append(o)
        cmd.append(nums[idx+1])

    print(f'cmd to eval: {cmd}')
    return eval(''.join(cmd))

def constructNumsObj(input):
    nums = {}
    lines = input.splitlines()
    for line in lines:
        l = line.split(':')
        total = l[0]
        n = l[1].strip().split(' ')
        nums[total] = n
    
    return nums

def getResult(true_vals):
    total = 0
    for val in true_vals:
        total += int(val)

    return total
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

    nums = constructNumsObj(input)
    true_vals = []

    for i in nums:
        total_combinations = 2**(len(nums[i])-1)
        op_spots = len(nums[i])-1
        print(f'Evaluating {i}: {nums[i]} - total_combinations: {total_combinations}')

        ops = ['+'] * op_spots
        test_val = i
        sum = evalOps(nums[i], ops)
        print(f'test_val: {test_val} sum: {sum}')      
        if compare(test_val,  sum):
            true_vals.append(test_val)       

    print(f'total calibration result: {getResult(true_vals)}')
if __name__ == "__main__":
    main()