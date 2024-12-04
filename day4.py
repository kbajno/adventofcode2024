from util import get_input
import re

    

def main():
    # Part 1
    input = get_input("4")

    # Word search conditions:
    # horizontal
    # vertical
    # diagonal
    # backwards
    # overlapping other words??
    # find ALL instances of XMAS
    print(input)
    word_search_matrix = []

    for idx, line in enumerate(input.rstrip()):
        split_line = line.rstrip().split()
        word_search_matrix.append(split_line)

    print(word_search_matrix)


if __name__ == "__main__":
    main()