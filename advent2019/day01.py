import utils

def parse_input(inp=None, day=1):
    """loads my input from disk, later add logic to handle user input"""
    if inp is None or inp == "":
        inp = utils.get_input(day)
    else:
        inp = inp.strip()
    return [int(mass) for mass in inp.splitlines()]

inp = parse_input()

# part 1
def calc_fuel(mass: int):
    """takes in a mass and returns the fuel required"""
    mass = mass // 3 - 2
    return mass if mass >= 0 else 0

def solve_1(inp=inp):
    return sum([calc_fuel(mass) for mass in inp])

# part 2
def total_fuel(mass: int):
    """takes in a mass and returns all the fuel required
       taking into account fuel needed for the fuel as well"""
    fuel_mass = calc_fuel(mass)
    
    if fuel_mass <= 0:
        return 0
    else:
        return fuel_mass + total_fuel(fuel_mass)

def solve_2(inp=inp):
    return sum([total_fuel(mass) for mass in inp])