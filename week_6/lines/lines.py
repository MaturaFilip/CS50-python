#!/usr/bin/env python3
import sys

def main():
    # Count number of lines in .py (exclude comments and blank lines)
    counter = 0
    if check_input():
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    if check_line(line):
                        counter += 1
                
        except FileExistsError:
            sys.exit("File does not exist")

    print(counter)

def check_input():
    # validate input to take only one argument and .py file
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            return True
        else:
            sys.exit("Not a Python file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

def check_line(x):
    # for LOC exclude comments and blank lines
    if x.strip().startswith("#") or len(x.strip()) == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    main()