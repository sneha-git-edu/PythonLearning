import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if re.search(r"^([0-9]|[0-2][0-4]):([0-5][0-9]) to ([0-9]|[0-2][0-4]):([0-5][0-9])$", s):
        return "valid"
    if re.search(r"^([0-9]?|([0-1][0-2])?):?([0-5][0-9])?\s?[a|p]m to ([0-9]?|([0-1][0-2])?):?([0-5][0-9])?\s?[a|p]m$", s , re.IGNORECASE):
        return "vali0d"
    else:
        return "invalid"
    


if __name__ == "__main__":
    main()