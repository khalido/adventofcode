import numpy as np
import requests

def get_input(day=1, year=2018):
    """takes in the day and year and returns the input"""
    try:
        with open(f'../inputs/{year}/{day}.txt') as f:
            data = f.read()
    except:
        print(f"Failed to load {year}/{day}.txt from disk, trying to get from github")
        url = f"https://github.com/khalido/adventofcode/raw/master/inputs/{year}/{day}.txt"
        data = requests.get(url).text
    return data
    #return data.strip().split(split_on)
        
def printmd(txt="## testing"):
    """displays a text string as markdown"""
    display(Markdown(txt))
    
def rotate(arr, num):
    """shits items in arr by num"""
    return np.roll(arr, num)