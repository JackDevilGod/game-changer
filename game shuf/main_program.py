from functions import *


def main():
    print(pygetwindow.getAllTitles())
    windows: list = []

    window_name = input("name of windows you want to switch between or enter to stop")

    while window_name != "":
        print(pygetwindow.getAllTitles())
        windows += [pygetwindow.getWindowsWithTitle(window_name)]
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

        shufflerrandom(windows, start, end, multiplier)
    else:
        time_of_switch: int = int(int(input(unit + " of switching")) * multiplier)

        shufflerfixed(windows, time_of_switch)
        

if __name__ == "__main__":
    main()
