import numpy as np
import requests

def get_input(day=1, year=2015, split_on="\n"):
    """takes in the day, year and a string to split on"""
    try:
        with open(f'../inputs//{year}/{day}.txt') as f:
            data = f.read().strip().split(split_on)
    except:
        url = f"https://github.com/khalido/adventofcode/raw/master/inputs/{year}/{day}.txt"
        data = requests.get(url).text
    
    return data.strip().split(split_on)
        
def rotate(arr, num):
    """shits items in arr by num"""
    return np.roll(arr, num)