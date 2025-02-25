#!/usr/bin/env python3

def main():
    question = (input("Greeting: ")).strip("$").lower()

    if question == "hello":
        return "$0"
    elif question.startswith("h"):
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    print(main())