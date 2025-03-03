#!/usr/bin/env python3
import sys
from PIL import Image
from PIL import ImageOps

# sys.argv 2 = name of existing csv, name of new csv with headers (first, last, house)

def main():

    if check_input():
        shirt = Image.open("shirt.png")
        image = Image.open(sys.argv[1])
        
        # get size of shirt image and then crop input image
        shirt_size = shirt.size
        image_croped = ImageOps.fit(image, shirt_size)

        # overlay image and save
        image_croped.paste(shirt, mask = shirt)
        image_croped.save(sys.argv[2])


                           
def check_input():
    # validate input to take only one argument and .csv file
    if len(sys.argv) == 3:
        if sys.argv[1].lower().endswith(".jpeg") or sys.argv[1].lower().endswith(".png") or sys.argv[1].lower().endswith("jpg"):
            end_1 = sys.argv[1].split(".")
            end_2 = sys.argv[2].split(".")
            if end_1[1] == end_2[1]:
                return True
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Not a jpeg / jpg / png file")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()