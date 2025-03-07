import re
import sys


def main():
    print(convert("9 AM to 5 PM"))
    #print(convert(input("Hours: ")))


def convert(s):
    pattern = re.search(r"\d{2} (AM|PM) to \d{2} (PM|AM)")
    if pattern:
        ...groups()


...


if __name__ == "__main__":
    main()