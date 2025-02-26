#!/usr/bin/env python3

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s.isalnum():
        letter = ""
        num = ""

        for i in s:
            if i.isdigit():
                num += i
            else:
                letter += i
        
        if len(num) != 0:
            if num[0] == "0":
                return False
        if (f"{letter}{num}") != s or (f"{letter}{num}")[0].isdigit():
            return False
        else:
            return True

if __name__ == "__main__":
    main()