import re
import sys



def main():
    print(count(input("Text: ")))


def count(s):
    # str to int
    x = re.findall(r"(\W|^)*um(\W)*", s, re.IGNORECASE)
    return len(x)


if __name__ == "__main__":
    main()