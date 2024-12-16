import copy
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

    # if p == True:
    print(f'cmd to eval: {cmd}')

    total = 0
    # print(f'nums: {nums}')
    for idx, num in enumerate(nums):
        if idx == (len(nums)-1):
            break
        else:
            cur_cmd = [str(total) if idx > 0 else str(num)]
            cur_cmd.append(str(op[idx]))
            cur_cmd.append(str(nums[idx+1]))

            exp = ''.join(cur_cmd)
            # print(exp)
            eval_result = eval(exp)  
            total = eval_result
            # print(f"total: {total}")
            # print(f"cmd: {cur_cmd} total: {total}")
            
    return total

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

def multRecursion(idx, nums, ops, sum, true_vals):
    if idx == len(ops):
        return None
    else:
        copy_ops = copy.deepcopy(ops)
        copy_ops[idx] = '*'
        eval_result = evalOps(nums, copy_ops)
        
        if compare(eval_result, sum):
            print(f'eval_result: {eval_result} sum: {sum}')     
            # print(f'We evaled: {evalOps(nums, copy_ops, True)}') 
            true_vals.append(eval_result)  
            print(f'true vals now: {true_vals}')
            return true_vals
        else:
            multRecursion(idx+1, nums, ops, sum, true_vals)


def main():
    input = get_input("7")
#     input = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""
#     input = """190: 10 19
# 3267: 81 40 27
# """
    nums = constructNumsObj(input)
    true_vals = []

    for i in nums:

        n = nums[i]
        sum = i
        print(f'Evaluating {sum}: {n}')
        if int(sum) == 98830:
            print('break')

        # Go from + to *
        op_spots = len(nums[i])-1
        ops = ['+'] * op_spots
        eval_result = evalOps(nums[i], ops)
        if compare(eval_result,  sum):
            print(f'eval_result: {eval_result} sum: {sum}')      
            # print(f'We evaled: {evalOps(nums, ops,)}') 
            true_vals.append(eval_result)  
            print(f'true vals now: {true_vals}')
            continue

        len_at_start = len(true_vals)
        len_true_vals = len(true_vals)
        multRecursion(0, nums[i], ops, sum, true_vals)
        len_after = len(true_vals)

        if len_after > len_true_vals:
            continue
        for o in range(op_spots):
            ops[o] = '*'
            len_true_vals = len(true_vals)
            multRecursion(0, nums[i], ops, sum, true_vals)
            len_after = len(true_vals)

            if len_after > len_true_vals:
                break
        len_at_mid = len(true_vals)
        if len_at_mid > len_at_start:
                continue   
            
        # go from * to +
        ops = ['*'] * op_spots
        len_true_vals = len(true_vals)
        multRecursion(0, nums[i], ops, sum, true_vals)
        len_after = len(true_vals)

        if len_after > len_true_vals:
            continue
        for o in range(op_spots):
            ops[o] = '+'
            len_true_vals = len(true_vals)
            multRecursion(0, nums[i], ops, sum, true_vals)
            len_after = len(true_vals)

            if len_after > len_true_vals:
                break
    print(f'total calibration result: {getResult(true_vals)}')
if __name__ == "__main__":
    main()