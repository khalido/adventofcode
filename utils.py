import numpy as np

def get_input(day=1, split_on="\n"):
    """takes in the day and a string to split on"""
    try:
        with open(f'inputs/{day}.txt') as f:
            data = f.read().strip().split(split_on)
        return data
    except:
        print("You must download the file and save into the inputs directory as {day_num}.txt")
        
def rotate(arr, num):
    """shits items in arr by num"""
    return np.roll(arr, num)