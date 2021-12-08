"""helper functions for advent of code

Todo:
1. replace the numpy based rotate function with a python equivalent
"""

import numpy as np
import requests


def get_input(day=1, year=2021, splitlines=False):
    """takes in the day, year and a string to split on"""
    try:
        with open(f"../inputs/{year}/{day}.txt") as f:
            data = f.read().strip()
    except:
        print(f"Failed to load {year}/{day}.txt from disk, trying to get from github")
        url = f"https://github.com/khalido/adventofcode/raw/master/inputs/{year}/{day}.txt"
        data = requests.get(url).text

    data = data.strip()

    if splitlines:
        data = data.splitlines()

    return data


def printmd(txt="## testing"):
    """displays a text string as markdown"""
    display(Markdown(txt))


def rotate(arr, num):
    """shits items in arr by num"""
    return np.roll(arr, num)
