#!/usr/bin/env python3

def main():
    get_time = input("What time is it? ")
    time = convert(get_time)

    if time >= 24:
        return None

    if (time >= 7.0 and time <= 8.0):
        return "breakfast time"
    elif (time >= 12.0 and time <= 13.0):
        return "lunch time"
    elif (time > 18.0 and time <= 19.0):
        return "dinner time"
    else:
        return None

def convert(time):
    time = time.split(":")

    hours = int(time[0])
    minutes = int(time[1]) / 60


    return float(hours + minutes)


if __name__ == "__main__":
    print(main())
