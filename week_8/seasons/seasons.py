import datetime
import sys
import re
import inflect

def main():
    get_date = input("Date of Birth: ")
    birth_date = get_valid_input(get_date)
    today = datetime.date.today()
    birth_date = datetime.date(birth_date[0], birth_date[1], birth_date[2])

    diff = today - birth_date
    minutes = diff.days * 24 * 60
    # convert minutes to text with inflect
    inflector = inflect.engine()
    to_words = inflector.number_to_words(minutes)
    to_words = to_words.replace(" and", "").capitalize()
    print(f"{to_words} minutes")

def get_valid_input(get_date):
    
    pattern = r"^(\d{4})-(\d{2})-(\d{2})$"
    try:
        match = re.findall(pattern, get_date)[0]
    except IndexError:
        sys.exit("Invalid input")



    match = list(map(int, match))

    if match[1] < 1 or match[1] > 12 or match[2] < 1 or match[2] > 31:
        sys.exit("Invalid input")
    return match

if __name__ == "__main__":
    main()