from util import get_input
import re

def main():
    input = get_input("3")
    matches = re.findall("mul\((\d{1,3}),(\d{1,3})\)",input)
    total = 0
    for match in matches:
        num1 = int(match[0])
        num2 = int(match[1])
        total += num1 * num2

    print(total)        

if __name__ == "__main__":
    main()