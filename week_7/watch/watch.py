import re
import sys

def main():
    # expect HTML input and extract youtube URL
    print(parse(input("HTML: ")))
    # if no url return None

def parse(s):
    x = re.findall((r"\"http[s]?:\/{2}w{0,3}\.?youtube\.com\/embed\/[A-Za-z0-9]+\""), s)
    if len(x) == 0:
        return None
    else:
        
        x = "".join(x).split("/")
        if x[0][1:] == "http:":
            output = f"https://youtu.be/{x[-1]}"
            output = output.replace('"','')
            return output
        else:
            output = f"{x[0]}//youtu.be/{x[-1]}"
            output = output.replace('"','')
            return output


if __name__ == "__main__":
    main()