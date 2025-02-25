#!/usr/bin/env python3

# ask for input and then print the same text but replace "space" with "..." 
def main():
    text = input()
    return text.replace(" ", "...")

if __name__ == "__main__":
    print(main())