from util import get_input
import re

def find_vertical_matches(x):
    print("vertical")
    matches = 0
    # forwards
    # print(f'max len: {len(x)}')
    for i in range(len(x)):
        for j in range(len(x)):
            # If we found an X, check for MAS
            if i+3 < len(x):
                if x[i][j] == 'X':
                    if x[i+1][j] == 'M':
                        if x[i+2][j] == 'A':
                            if x[i+3][j] == 'S':
                                matches += 1
            # else:
            #     print(f'Skipping index {i} because i+3 is {i+3} and max len is {len(x)}')

    # backwards
    for i in range(len(x)-1, -1, -1):
        # print(i)
        for j in range(len(x)):
            # If we found an X, check for MAS
            if i-3 < -1:
                if x[i][j] == 'X':
                    if x[i-1][j] == 'M':
                        if x[i-2][j] == 'A':
                            if x[i-3][j] == 'S':
                                matches += 1

    return matches
 
def find_horizontal_matches(x):
    print("horizontal")
    # forwards

    # backwards

def find_diagonal_matches(x):
    print("diagonal")   
    # forwards

    # backwards

def main():
    # Part 1
    input = get_input("4")
    word_search = str.splitlines(input)

    # for idx, line in enumerate(input.rstrip()):
    #     print(input)
    #     # split_line = line.rstrip().split()
    #     # word_search_matrix.append([line.rstrip()])

    print(word_search)

    # horizontal
    print(find_vertical_matches(word_search))
    # vertical
    # diagonal
    # backwards
    # overlapping other words??
    # find ALL instances of XMAS
if __name__ == "__main__":
    main()