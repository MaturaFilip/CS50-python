#!/usr/bin/env python3
import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()

    if len(sys.argv) == 1:
        get_input = input("Input: ")
        get_font = random.choice(figlet.getFonts())
        figlet.setFont(font=get_font)
        print(figlet.renderText(get_input))

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
        get_input = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(get_input))
    else:
        sys.exit("Wrong command-line arguments")

if __name__ == "__main__":
    main()
