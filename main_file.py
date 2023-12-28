"""
the file to run the program
"""
from general_functions import *


def main():
    file = open(input("filepath to file"), "rw")
    print(file.read())

    if mode_select() == "encrypt":
        # encrypt code
    else:
        # decrypt code


if __name__ == "__main__":
    main()
