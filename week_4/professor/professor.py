#!/usr/bin/env python3
import random

def main():
    attempt = 0
    round = 0
    score = 0
    selected_level = get_level()

    while round != 10:
        first_num = generate_integer(selected_level)
        second_num = generate_integer(selected_level)
        answer = first_num + second_num

        while attempt != 3:
            try:
                get_answer = int(input(f"{first_num} + {second_num} = "))
                if get_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempt += 1
            except ValueError:
                print("EEE")
                attempt += 1

        if attempt == 3:
            print(f"{first_num} + {second_num} = {answer}")

        round += 1
        attempt = 0

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            get_level = int(input("Level: "))
            if get_level >= 1 and get_level <= 3:
                return get_level
        except ValueError:
            print("The level must be integer 1, 2 or 3")
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()