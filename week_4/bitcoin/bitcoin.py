#!/usr/bin/env python3
import requests
import sys

def main():
    bitcoin_num = check_input()
    try:
        url = f"https://api.coincap.io/v2/assets"
        response = requests.get(url) # return response object
        res = response.json()
        price_usd = float(res["data"][0]["priceUsd"])
    except requests.RequestException:
        sys.exit()

    print(f"${(bitcoin_num*price_usd):,.4f}")

def check_input():
    if len(sys.argv) == 1:
        print(f"Missing command-line argument")
    elif len(sys.argv) > 2:
        print (f"Too many command-line arguments")
    else:
        try:
            to_float = float(sys.argv[1])
            return to_float
        except ValueError:
            sys.exit("Cannot convert input to float, terminating the program")

if __name__ == "__main__":
    main()
