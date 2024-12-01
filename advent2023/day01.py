import marimo

__generated_with = "0.1.63"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    import re
    import utils
    return mo, re, utils


@app.cell
def __(mo):
    mo.md(
        """
    # [Day 1: Trebuchet?!](https://adventofcode.com/2023/day/1)
    Get the first and last digit in a string."""
    )
    return


@app.cell
def __(utils):
    test = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""

    inp = utils.get_input(1)

    def parse(inp: str = test):
        return inp.splitlines()

    parse()
    return inp, parse, test


@app.cell
def __(inp, parse, test):
    def get_nums(line: str) -> int:
        ans = ""

        for c in line:
            if c.isdigit():
                ans += c
                break

        for c in line[::-1]:
            if c.isdigit():
                ans += c
                break

        return int(ans)


    def solve(inp: str = test):
        lines = parse(inp)
        ans = 0
        for line in lines:
            ans += get_nums(line)
        return ans


    assert solve() == 142
    solve(inp)
    return get_nums, solve


@app.cell
def __(mo):
    mo.md(
        """
        # Part 2
        Numbers as text now also count as, so besides looking for digits, consider one, two ... nine as well.
        """
    )

    test2 = """two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen"""
    return test2,


@app.cell
def __(mo):
    mo.md("Using a simple dict to covert word nums to numbers. As a somewhat hack I added the first and last digit of the word back to stop the solution breaking.")
    return


@app.cell
def __():
    nums = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",}
    return nums,


@app.cell
def __(get_nums, inp, nums, parse, test2):
    def words_to_nums(line: str) -> str:
        """replaces text numbers with digits"""
        for word, num in nums.items():
            line = line.replace(word, num)
        return line

    def solve_2(inp: str = test2) -> int:
        lines = parse(inp)
        ans = 0
        for line in lines:
            line = words_to_nums(line)
            ans += get_nums(line)
        return ans

    assert solve_2() == 281
    solve_2(inp)
    return solve_2, words_to_nums


if __name__ == "__main__":
    app.run()
