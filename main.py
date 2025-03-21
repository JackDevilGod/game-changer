from functions.functions import shuffler_fixed, shuffler_random
from pygetwindow import getAllTitles, getWindowsWithTitle


def main():
    print(getAllTitles())
    windows: list = []

    window_name = input("name of windows you want to switch between or enter to stop")

    while window_name != "":
        print(getAllTitles())
        windows += [getWindowsWithTitle(window_name)]
        print(windows)
        window_name = input("name of windows you want to switch between or enter to stop")

    choice: str = input("choose random or fixed").lower()

    while choice != "random" or choice != "fixed":
        choice = input("choose random or fixed").lower()

    unit: str = " "
    multiplier: int | float = 0

    while multiplier == 0:
        unit = input("select unit (ms,s,m)").lower()

        if unit == "ms":
            multiplier = 0.01
        elif unit == "s":
            multiplier = 1
        elif unit == "m":
            multiplier = 60

    if choice == "random":
        start = int(input("min " + unit + " of switching"))
        end = int(input("max " + unit + " of switching"))

        shuffler_random(windows, start, end, multiplier)
    else:
        time_of_switch: int = int(int(input(unit + " of switching")) * multiplier)

        shuffler_fixed(windows, time_of_switch)


if __name__ == "__main__":
    main()
