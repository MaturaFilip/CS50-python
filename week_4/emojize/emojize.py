#!/usr/bin/env python3
import emoji

def main():
    get_input = input("Input: ")
    print("Output: " + emoji.emojize(get_input, language="alias"))

if __name__ == "__main__":
    main()