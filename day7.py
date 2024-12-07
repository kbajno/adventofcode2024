from util import get_input

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
    print(nums)


if __name__ == "__main__":
    main()