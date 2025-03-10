import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # str to int
    x = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(x)

if __name__ == "__main__":
    main()
