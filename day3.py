from util import get_input
import re

def get_total_of_substring(substr):
    matches = re.findall("mul\((\d{1,3}),(\d{1,3})\)",substr)
    total = 0
    for match in matches:
        num1 = int(match[0])
        num2 = int(match[1])
        total += num1 * num2

    return total
    

def main():
    # Part 1
    input = get_input("3")
    print(f"Part 1: {get_total_of_substring(input)}")

    # Part 2
    res = input.split("don't()")
    total = 0    

    for idx, r in enumerate(res):
        if idx == 0:
            total += get_total_of_substring(res[0])
        else:
            to_count = r.split("do()")
            for idx, tc in enumerate(to_count):
                if idx != 0:
                    total += get_total_of_substring(tc)

    print(f"Part 2: {total}")

if __name__ == "__main__":
    main()