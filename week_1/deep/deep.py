#!/usr/bin/env python3

def main():
    question = (input("What is the answer to the Great Question of Life, the Universe and Everything? ")).strip().lower()

    if question == "42" or question == "forty-two" or question == "forty two":
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    print(main())