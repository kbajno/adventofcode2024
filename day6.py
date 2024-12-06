from util import get_input

def locateGuard(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '^':
                return i, j

def main():
    # input = get_input("6").strip()
    input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split("\n")

    print(locateGuard(input))
if __name__ == "__main__":
    main()