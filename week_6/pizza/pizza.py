#!/usr/bin/env python3
import sys
import csv
import tabulate

def main():
    pizza = []
    if check_input():
       with open(sys.argv[1]) as file:
           reader = csv.DictReader(file)
           type, small, large = reader.fieldnames
           for row in reader:
               pizza.append({type: row[type], small: row[small], large: row[large]})

    print(tabulate.tabulate(pizza, headers = "keys", tablefmt="grid"))
               
def check_input():
    # validate input to take only one argument and .csv file
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            return True
        else:
            sys.exit("Not a csv file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()