#!/usr/bin/env python3
import random
import sys

def main():

    while True:
        try:
            get_level = int(input("Level: "))
            if get_level > 0:
                random_number = generate_number(get_level)
                while True:
                    try:
                        get_guess = int(input("Guess: "))
                        if get_guess > 0:
                            if get_guess < random_number:
                                print("Too small!")
                                continue
                            elif get_guess > random_number:
                                print("Too large!")
                                continue
                            else:
                                print("Just right!")
                                sys.exit()

                    except ValueError:
                        pass
        
        except ValueError:
            pass


def generate_number(n):
    n += 1
    return random.randrange(1,n)



if __name__ == "__main__":
    main()