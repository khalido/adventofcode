"""helper functions for advent of code

Todo:
1. replace the numpy based rotate function with a python equivalent
"""

import numpy as np
import requests


def get_input(day: int = 1, year: int = 2023, splitlines=False) -> str:
    """takes in the day, year and a string to split on.
    Looks for the AOC input in a inputs folder, or at github"""

    try:
        with open(f"inputs/{day}.txt") as f:
            data = f.read()
    except:
        print(
            f"Failed to load advent{year}/inputs/{day}.txt from disk, trying to get from github"
        )
        url = f"https://github.com/khalido/adventofcode/raw/master/advent{year}/inputs/{day}.txt"
        data = requests.get(url).text

    if splitlines:
        data = data.splitlines()

    return data


def printmd(txt: str = "## testing"):
    """displays a text string as markdown"""
    display(Markdown(txt))


def rotate(arr, num):
    """shits items in arr by num"""
    return np.roll(arr, num)
