import pygetwindow


def temp():
    game_windows = pygetwindow.getWindowsWithTitle("SOULS")

    game_windows[0].activate()


def main():
    temp()


if __name__ == "__main__":
    main()
