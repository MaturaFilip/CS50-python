import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)"
    match = re.match(pattern, s)
    if match:
        hr_1, min_1, am_pm_1, hr_2, min_2, am_pm_2 = match.groups()

        if min_1 == None:
            min_1 = 0
        if min_2 == None:
            min_2 = 0

        try:
            time = [hr_1, min_1, hr_2, min_2]
            time = list(map(int, time))
        except ValueError:
            pass

        if time[1] >= 60 or time[3] >= 60 or time[0] > 12 or time[2] > 12:
            raise ValueError

        if am_pm_1 == "AM":
            if time[0] == 12:
                time[0] = 0

        if am_pm_2 == "AM":
            if time[2] == 12:
                time[2] = 0

        if am_pm_1 == "PM":
            if time[0] != 12:
                time[0] += 12

        if am_pm_2 == "PM":
            if time[2] != 12:
                time[2] += 12

        if time[0] == (time[2]-8):
            return f"{time[0]:02}:{time[1]:02} to {time[2]:02}:{time[3]:02}"
        else:
            raise ValueError

if __name__ == "__main__":
    main()