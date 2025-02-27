#!/usr/bin/env python3

def main():
    shop_list = {}
    while True:
        try:
            get_item = input().upper()

            if get_item not in shop_list:
                shop_list[get_item] = 1
            else:
                shop_list[get_item] += 1

        except (EOFError):
            shop_list = dict(sorted(shop_list.items()))
            for k, v in shop_list.items():
                print(f"{v} {k}")
            break

if __name__ == "__main__":
    main()