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
    
    print('we should be done?')
    return map, True

def moveLeft(map, guard_i, guard_j):
    map[guard_i][guard_j] = 'X'
    ## get the row, move backwards through J
    for j in range(len(map[guard_i])-1, -1, -1):
        if j >= guard_j:
            continue
        print(f"j is: {j}")
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

    done = False
    while(done != True):
        print('START')
        prettyPrint(map)

        print('MOVING UP')
        i, j = locateGuard(map)
        print(f'GUARD IS AT: {i}, {j}')
        map, done = moveUp(map, i, j)
        if done == True:
            break
        prettyPrint(map)

        print('MOVING RIGHT')
        i, j = locateGuard(map)
        print(f'GUARD IS AT: {i}, {j}')
        map, done = moveRight(map, i, j)
        if done == True:
            break
        prettyPrint(map)

        print('MOVING DOWN')
        i, j = locateGuard(map)
        print(f'GUARD IS AT: {i}, {j}')
        map, done = moveDown(map, i, j)
        if done == True:
            break
        prettyPrint(map)

        print('MOVING LEFT')
        i, j = locateGuard(map)
        print(f'GUARD IS AT: {i}, {j}')
        map, done = moveLeft(map, i, j)
        if done == True:
            break
        prettyPrint(map)

    print('ALL DONE')
    prettyPrint(map)

    total = 0
    for m in map:
        total += m.count('X')
  
    print(f'total: {total}')
if __name__ == "__main__":
    main()