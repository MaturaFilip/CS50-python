#!/usr/bin/env python3

def main():

    get_input = input("Expression: ").split(" ")

    x = float(get_input[0])
    y = get_input[1]
    z = float(get_input[2])

    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z
        case default:
            return "bad input"

if __name__ == "__main__":
    print(main())