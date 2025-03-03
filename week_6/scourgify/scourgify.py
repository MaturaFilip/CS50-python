#!/usr/bin/env python3
import sys
import csv
import tabulate

# sys.argv 2 = name of existing csv, name of new csv with headers (first, last, house)

def main():
    characters = []
    if check_input():
       with open(sys.argv[1]) as file:
           reader = csv.DictReader(file)
           for row in reader:
                # clean the data (name column to first and last)
                record = {}
                record["house"] = row["house"]
                record["last"] = row["name"].split(",")[0]
                record["first"] = row["name"].split(",")[1].strip()
                characters.append(record)

    
    # write output to csv
    with open(sys.argv[2], "w") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)
                           
def check_input():
    # validate input to take only one argument and .csv file
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv"):
            return True
        else:
            sys.exit("Not a csv file")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()