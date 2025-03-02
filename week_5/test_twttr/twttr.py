#!/usr/bin/env python3

def main():    
    get_string = input("Input: ")
    x = shorten(get_string)
    print(x)

def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

    twttr = ""
    for letter in word:
        if letter in vowels:
            continue
        else:
            twttr += letter
    
    return f"{twttr}"

if __name__ == "__main__":
    main()
