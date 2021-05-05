#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: May 2021
# This program checks the number's month


def main():
    # this function checks the number's month

    # input
    number = int(input("Enter a number of a month: "))
    print("")

    # process & output
    if number == 1:
        print("January")
    elif number == 2:
        print("February")
    elif number == 3:
        print("March")
    elif number == 4:
        print("April")
    elif number == 5:
        print("May")
    elif number == 6:
        print("June")
    elif number == 7:
        print("July")
    elif number == 8:
        print("August")
    elif number == 9:
        print("September")
    elif number == 10:
        print("October")
    elif number == 11:
        print("November")
    elif number == 12:
        print("December")
    else:
        print("Invalid number")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
