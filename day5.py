from util import get_input


def main():
    input = get_input("5")
    split_input = input.split("\n\n")
    rules = split_input[0].rstrip()
    pages = split_input[1].rstrip()
if __name__ == "__main__":
    main()