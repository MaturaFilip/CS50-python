#!/usr/bin/env python3
#import inflect
import sys


def main():
    #p = inflect.engine()
    names = []
    
    while True:
        try:
            get_name = input("Name: ")
            names.append(get_name)

        except (EOFError):
            if len(names) > 0 and len(names) <= 1:
                print(f"Adieu, adieu, to {"".join(names)}")
            elif len(names) <= 2:
                names.insert(-1, "and")
                message = f"Adieu, adieu, to {", ".join(names)}"
                firt_name = f"{names[0]},"
                first_name_without_comma = f"{names[0]}"
                message = message.replace("and,", "and").replace(firt_name, first_name_without_comma)
                print(message)
            elif len(names) > 2:
                names.insert(-1, "and")
                message = f"Adieu, adieu, to {", ".join(names)}"
                message = message.replace("and,", "and")
                print(message)
            sys.exit()

if __name__ == "__main__":
    main()
