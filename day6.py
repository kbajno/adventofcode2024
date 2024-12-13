import copy
import numpy as np
from util import get_input

def locateGuard(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '^' or map[i][j] == '>' or map[i][j] == 'v' or map[i][j] == '<':
                return i, j
            
def moveUp(map, guard_i, guard_j):
    map[guard_i][guard_j] = 'X'
    for i in range(len(map[:guard_i])-1, -1, -1):
        # print(f"i is: {i}")
        # print(f"map[i][guard_j] {map[i][guard_j]}")
        if map[i][guard_j] == '.':
            map[i][guard_j] = 'X'
        elif map[i][guard_j] == '#':
            # Turn 90 degrees at obstacle
            map[i+1][guard_j] = '>'
            return map, False
        
    return map, True

def moveDown(map, guard_i, guard_j):
    map[guard_i][guard_j] = 'X'
    # print(map[guard_i:])
    for i in range(len(map[guard_i])):
        if i <= guard_i:
            continue
        # print(f"i is: {i}")
        # print(f"map[i][guard_j] {map[i][guard_j]}")
        if map[i][guard_j] == '.':
            map[i][guard_j] = 'X'
        elif map[i][guard_j] == '#':
            # Turn 90 degrees at obstacle
            map[i-1][guard_j] = '<'
            return map, False
    
    # print('we should be done?')
    return map, True

def moveLeft(map, guard_i, guard_j):
    map[guard_i][guard_j] = 'X'
    ## get the row, move backwards through J
    for j in range(len(map[guard_i])-1, -1, -1):
        if j >= guard_j:
            continue
        # print(f"j is: {j}")
        # # print(f"map[i][guard_j] {map[i][guard_j]}")
        if map[guard_i][j] == '.':
            map[guard_i][j] = 'X'
        elif map[guard_i][j] == '#':
            # Turn 90 degrees at obstacle
            map[guard_i][j+1] = '^'
            return map, False
        
    return map, True

def moveRight(map, guard_i, guard_j):
    map[guard_i][guard_j] = 'X'
    for j in range(len(map[guard_i])):
        if j <= guard_j:
            continue
        # print(f"j is: {j}")
        # # print(f"map[i][guard_j] {map[i][guard_j]}")
        if map[guard_i][j] == '.':
            map[guard_i][j] = 'X'
        elif map[guard_i][j] == '#':
            # Turn 90 degrees at obstacle
            map[guard_i][j-1] = 'v'
            return map, False
        
    return map, True

def prettyPrint(map):
    print(np.matrix(map))    

def getPotentialObstructionCoordinates(map):
    coords = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'X':
                coords.append(f'{i},{j}')
    return coords

def main():
    input = get_input("6").strip()
#     input = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""
    map = str.splitlines(input)
    for idx, m in enumerate(map):
        map[idx] = list(m)

    orig_map = copy.deepcopy(map)
    orig_guard_i, orig_guard_j = locateGuard(orig_map)
    print(f'orig: {orig_guard_i}, {orig_guard_j}')
    done = False
    while(done != True):
        # print('START')
        # prettyPrint(map)

        # print('MOVING UP')
        i, j = locateGuard(map)
        # print(f'GUARD IS AT: {i}, {j}')
        map, done = moveUp(map, i, j)
        if done == True:
            break
        # prettyPrint(map)

        # print('MOVING RIGHT')
        i, j = locateGuard(map)
        # print(f'GUARD IS AT: {i}, {j}')
        map, done = moveRight(map, i, j)
        if done == True:
            break
        # prettyPrint(map)

        # print('MOVING DOWN')
        i, j = locateGuard(map)
        # print(f'GUARD IS AT: {i}, {j}')
        map, done = moveDown(map, i, j)
        if done == True:
            break
        # prettyPrint(map)

        # print('MOVING LEFT')
        i, j = locateGuard(map)
        # print(f'GUARD IS AT: {i}, {j}')
        map, done = moveLeft(map, i, j)
        if done == True:
            break
        # prettyPrint(map)

    # print('ALL DONE')
    # prettyPrint(map)

    total = 0
    for m in map:
        total += m.count('X')
  
    print(f'total: {total}')

    # part 2: find all the infinite loop spots
    # put a new # at each location, and run it through the done checker
    # maximum amount of runs though the done checker will be  10k
    # if it hasn't finished by then, count it as an infinite loop +1 to obstruction

    potential_obstruction_coordinates = getPotentialObstructionCoordinates(map)
    print(potential_obstruction_coordinates)

    diff_positions = 0
    for coords in potential_obstruction_coordinates:
        test_map = copy.deepcopy(orig_map)
        c = coords.split(',')
        if orig_guard_i == int(c[0]) and  orig_guard_j == int(c[1]):
            continue

        test_map[int(c[0])][int(c[1])] = '#'

        done = False
        x = 0
        while(done != True):
            if (x == 100):
                break
            # print('START')
            # prettyPrint(test_map)

            # print('MOVING UP')
            i, j = locateGuard(test_map)
            # print(f'GUARD IS AT: {i}, {j}')
            test_map, done = moveUp(test_map, i, j)
            if done == True:
                break
            # prettyPrint(map)

            # print('MOVING RIGHT')
            i, j = locateGuard(test_map)
            # print(f'GUARD IS AT: {i}, {j}')
            test_map, done = moveRight(test_map, i, j)
            # print(f'DONE IS: {done}')
            if done == True:
                # print('we should break')
                break
            # prettyPrint(map)
            # print('but were not?')
            # print('MOVING DOWN')
            i, j = locateGuard(test_map)
            # print(f'GUARD IS AT: {i}, {j}')
            test_map, done = moveDown(test_map, i, j)
            if done == True:
                break
            # prettyPrint(map)

            # print('MOVING LEFT')
            i, j = locateGuard(test_map)
            # print(f'GUARD IS AT: {i}, {j}')
            test_map, done = moveLeft(test_map, i, j)
            if done == True:
                break
            # prettyPrint(map)
            x = x + 1
        # print('ALL DONE')
        # prettyPrint(map)
        if x == 100:
            diff_positions = diff_positions + 1
        print(f'Checking cords: {coords}, diff_positions: {diff_positions}')

    print(f'diff_positions: {diff_positions}')

if __name__ == "__main__":
    main()