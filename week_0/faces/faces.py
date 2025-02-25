#!/usr/bin/env python3

# ask for input. If text contain smile face :) or sad face :(, convert it to emoji.
def main():
    text = input()
    return text.replace(":)", "🙂").replace(":(", "🙁")

if __name__ == "__main__":
    print(main())