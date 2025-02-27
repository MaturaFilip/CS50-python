#!/usr/bin/env python3

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        get_date = input("Date: ") # 8/9/1637 -> 1636-08-09
        try:
            if "/" in get_date:
                month, day, year = map(int, get_date.split("/"))
                if day > 0 and day <= 31 and month > 0 and month <= 12:
                    print(f"{year}-{month:02}-{day:02}")
                    break

            elif "," in get_date:
                get_date = get_date.replace(",", "")
                month, day, year = map(str, get_date.split(" "))

                if month in months:
                    day = int(day)
                    year = int(year)
                    month = int(months.index(month)) + 1
                    if day > 0 and day <= 31 and month > 0 and month <= 12:
                        print(f"{year}-{month:02}-{day:02}")
                        break   
        except:
            pass    

if __name__ == "__main__":
    main()