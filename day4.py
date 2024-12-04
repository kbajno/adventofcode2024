from util import get_input
import re

def find_vertical_matches(x):
    matches = 0
    # forwards

    for i in range(len(x)):
        for j in range(len(x[i])):
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
        for j in range(len(x[i])):
            # If we found an X, check for MAS
            if i-3 > -1:
                if x[i][j] == 'X':
                    if x[i-1][j] == 'M':
                        if x[i-2][j] == 'A':
                            if x[i-3][j] == 'S':
                                matches += 1

    return matches
 
def find_horizontal_matches(x):
    matches = 0

    # forwards
    for i in range(len(x)):
        for j in range(len(x[i])):
            # If we found an X, check for MAS
            if j+3 < len(x[i]):
                if x[i][j] == 'X':
                    if x[i][j+1] == 'M':
                        if x[i][j+2] == 'A':
                            if x[i][j+3] == 'S':
                                matches += 1
            # else:
            #     print(f'Skipping index {j} because j+3 is {j+3} and max len is {len(x[i])}')

    # # backwards
    for i in range(len(x)):
        for j in range(len(x)-1, -1, -1):
            # If we found an X, check for MAS
            if j-3 > -1:
                if x[i][j] == 'X':
                    if x[i][j-1] == 'M':
                        if x[i][j-2] == 'A':
                            if x[i][j-3] == 'S':
                                matches += 1

    return matches

def find_diagonal_matches(x):
    matches = 0
    # direction 1 \
    # forwards
    for i in range(len(x)):
        for j in range(len(x[i])):
            # If we found an X, check for MAS
            if i+3 < len(x) and j+3 < len(x[i]):
                if x[i][j] == 'X':
                    if x[i+1][j+1] == 'M':
                        if x[i+2][j+2] == 'A':
                            if x[i+3][j+3] == 'S':
                                matches += 1
            # else:
            #     print(f'Skipping forward match for index {i},{j} - i,j+3 is {i+3},{j+3} and max len is {len(x)},{len(x[i])}')

    # backwards
    for i in range(len(x)-1, -1, -1):
        for j in range(len(x)-1, -1, -1):
            # If we found an X, check for MAS
            if i-3 > -1 and j-3 > -1:
                if x[i][j] == 'X':
                    if x[i-1][j-1] == 'M':
                        if x[i-2][j-2] == 'A':
                            if x[i-3][j-3] == 'S':
                                matches += 1
            # else:
            #     print(f'Skipping backward match for index {i},{j} - i,j+3 is {i+3},{j+3} and max len is {len(x)},{len(x[i])}')
    # direction 2 /
    # forwards
    for i in range(len(x)-1, -1, -1):
        for j in range(len(x[i])):
            # If we found an X, check for MAS
            if i-3 > -1 and j+3 < len(x[i]):
                if x[i][j] == 'X':
                    if x[i-1][j+1] == 'M':
                        if x[i-2][j+2] == 'A':
                            if x[i-3][j+3] == 'S':
                                matches += 1
            # else:
            #     print(f'Skipping forward match for index {i},{j} - i,j+3 is {i+3},{j+3} and max len is {len(x)},{len(x[i])}')

    # backwards
    for i in range(len(x)):
        for j in range(len(x)-1, -1, -1):
            # If we found an X, check for MAS
            if i+3 < len(x) and j-3 > -1:
                if x[i][j] == 'X':
                    if x[i+1][j-1] == 'M':
                        if x[i+2][j-2] == 'A':
                            if x[i+3][j-3] == 'S':
                                matches += 1
            # else:
            #     print(f'Skipping backward match for index {i},{j} - i,j+3 is {i+3},{j+3} and max len is {len(x)},{len(x[i])}')

    return matches

def main():
    # Part 1
    input = get_input("4")
    word_search = str.splitlines(input)

    # print(word_search)

    # horizontal
    horizontal_total = find_horizontal_matches(word_search)
    print(f"horizontal_total: {horizontal_total}")

    # vertical
    vertical_total = find_vertical_matches(word_search)
    print(f"vertical_total: {vertical_total}")

    # diagonal
    diagonal_total = find_diagonal_matches(word_search)
    print(f"diagonal_total: {diagonal_total}")

    # find ALL instances of XMAS
    print(f"TOTAL: {horizontal_total + vertical_total + diagonal_total}")
if __name__ == "__main__":
    main()