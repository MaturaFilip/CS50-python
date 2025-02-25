#!/usr/bin/env python3

# ask for input (mass as integer) and calculate E in E=mc^2
def main():
    m = int(input("m: "))
    c = 300000000
    return f"E: {m*(c**2)}"

if __name__ == "__main__":
    print(main())