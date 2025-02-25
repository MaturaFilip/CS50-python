#!/usr/bin/env python3

def main():

    suffix = input("File name: ").lower().strip()

    if "." in suffix:
        suffix = suffix.rsplit(".")[-1].strip()
    else:
        return "application/octet-stream"

    if suffix == "gif" or suffix == "png":
        return f"image/{suffix}"
    if suffix == "jpg" or suffix == "jpeg":
        return "image/jpeg"
    elif suffix == "pdf" or suffix == "zip":
        return f"application/{suffix}"
    elif suffix == "txt":
        return f"text/plain"
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    print(main())