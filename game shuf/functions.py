import random
import time

import pygetwindow


def shufflerrandom(game_windows: list, start: int, end: int, multiplier: int):
    current_window: int = 0
    next_window: int = 0

    game_windows[0].minimize()
    game_windows[0].maximize()

    while True:
        time.sleep(random.randint(start, end) * multiplier)

        while current_window == next_window:
            next_window = random.randint(0, len(game_windows) - 1)

        game_windows[next_window].minimize()
        game_windows[next_window].maximize()

        current_window = next_window


def shufflerfixed(game_windows: list, time_of_switch: int):
    current_window: int = 0
    next_window: int = 0

    game_windows[0].minimize()
    game_windows[0].maximize()

    while True:
        time.sleep(time_of_switch)

        while current_window == next_window:
            next_window = random.randint(0, len(game_windows) - 1)

        game_windows[next_window].minimize()
        game_windows[next_window].maximize()

        current_window = next_window


def main():
    return


if __name__ == "__main__":
    main()
