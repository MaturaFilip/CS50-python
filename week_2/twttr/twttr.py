#!/usr/bin/env python3

def main():    
    # remove vowels
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    get_string = input("Input: ")

    twttr = ""
    for letter in get_string:
        if letter in vowels:
            continue
        else:
            twttr += letter
    
    return f"Output: {twttr}"

if __name__ == "__main__":
    print(main())