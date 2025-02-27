#!/usr/bin/env python3

def main():
    x = get_input("Fraction: ")
    print(x)


def get_input(num):
    while True:
        try:
            x, y = map(int, input(num).split("/"))

            if x <= y:
                perc = round((x / y)*100)
                if perc >= 99:
                    return "F"
                if perc <= 1:
                    return "E"
                
                return f"{perc}%"

        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()