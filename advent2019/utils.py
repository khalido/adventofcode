import numpy as np
import requests

def get_input(day: int = 1, year: int = 2019):
    """takes in the day and year and returns the input"""
    try:
        with open(f'../inputs/{year}/{day}.txt') as f:
            data = f.read()
    except:
        print(f"Failed to load {year}/{day}.txt from disk, trying to get from github")
        url = f"https://github.com/khalido/adventofcode/raw/master/inputs/{year}/{day}.txt"
        data = requests.get(url).text
    return data.strip()
    #return data.strip().split(split_on)
        
def get_code(day=1):
    with open(f'{year}/{day}.txt') as f:
        data = f.read()

def printmd(txt="## testing"):
    """displays a text string as markdown"""
    display(Markdown(txt))
    
def rotate(arr, num):
    """shits items in arr by num"""
    return np.roll(arr, num)

def convert_to_grid(inp: str):
    """takes in grid as a string and returns a 2d grid representation"""
    strings = inp.strip().splitlines()
    rows = [np.array([c for c in row]) for row in strings]
    return np.array(rows, dtype="U")