#!/usr/bin/env python3

def main():
    get_variable = input("camelCase: ")
    snake_case = ""

    for letter in get_variable:
        if letter.isupper():
            snake_case += f"_{letter.lower()}"
        else:
            snake_case += letter
    return snake_case
    
if __name__ == "__main__":
    print(main())