#!/usr/bin/env python3

def main():    
    # price for coke
    amount_due = 50

    while amount_due != 0:

        print(f"Amount Due: {amount_due}")
        get_coin = int(input("Insert Coin (25, 10, 5): "))

    # ignore every coin except 25, 10, 5
        if get_coin == 25 or get_coin == 10 or get_coin == 5:
            amount_due -= get_coin
        else:
            continue

        if amount_due <= 0:
            print(f"Change Owed: {abs(amount_due)}")
            break
    
if __name__ == "__main__":
    main()