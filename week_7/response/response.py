import validators

def main():
    print(is_valid(input("What's your email address? ")))

def is_valid(s):
    # str to int
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
