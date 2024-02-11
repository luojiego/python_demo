#!/usr/bin/env python3

import datetime

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # print(f"{year} is a leap year")
                return True
            else:
                return False
                # print(f"{year} is not a leap year")
        else:
            return True
            # print(f"{year} is a leap year")
    else:
        return False
        # print(f"{year} is not a leap year")

is_leap_year(1900) is False
dir(datetime)

# def main():
#     is_leap_year()

# if __name__ == "__main__":
#     main()