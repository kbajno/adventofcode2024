import argparse

parser = argparse.ArgumentParser(
                    prog='AoC Day 1',
                    description='',
                    epilog='')

def main():
    parser.add_argument('filename')
    args = parser.parse_args()

    ## PART 1
    list1 = []
    list2 = []
    with open(args.filename) as file:
        for line in file:
                x = line.rstrip().split("   ")
                list1.append(x[0])
                list2.append(x[1])
    
    list1.sort()
    list2.sort()

    running_total = 0
    for idx, val in enumerate(list1):
         diff = abs(int(list1[idx]) - int(list2[idx]))
         running_total += diff
         print(f"{list1[idx]} - {list2[idx]} DIFF {diff}")

    print(running_total)

    ## Part 2

    # create a dict of the numbers in part 1, with the val being how many times it appears in list 2
    # then math

    new_dict = {}

    for idx, val in enumerate(list1):
        number_of_occurances = 0
        for val2 in list2:
            if val2 == val:
                number_of_occurances += 1
        new_dict[val] = number_of_occurances

    similarity_score = 0
    for val in list1:
         similarity_score += int(val) * int(new_dict[val])

    print(similarity_score)
         

         


# each location being checked, marked with star
# historian must be in one of first fifty places
# list of locations currently empty

# list found in Chief's office with locations, listed by unique id (location ID)
# two lists 

# pair up the smallest number in left list with smallest number in the right list
# figure out how far apart the two numbers on, and add up all the distances

# parse left and right list into 2 arrays
# sort arrays in increasing numerical order
# get absolute value of the difference
# add it together

if __name__ == "__main__":
    main()