## [Advent of Code 2023](https://adventofcode.com/2023)

* Day 1 - tried [marimo](https://marimo.io/) for this, interesting.  The problem itself was just a warmup, reading numbers from a string and adding them up.
* Day 2 - a simple game. This was easy, involved regex to grab numbers and a switch case statement.
* Day 3 - This was a grid problem, and all grid problems are pretty similar, except this has a twist - Objects in the grid can take up multiple points, so that makes defining the adjacent function a bit tricky. 
* Day 4: This was easy, but required a bit of thinking of how to manage multiple copies. It looked like a recursion problem but didn't need recursion to solve.
* Day 5: Converting numbers from one to the another. The trick here was using computation instead of a dictionary to store all the conversions - with the dict my computer ran out of memory, so the only way to do it was to compute the answer.
* Day 7: This was fun - I had never implemented a poker game, and this was an excuse to make a simple one. The tricky thing here was how to compare one hand to all other hands to rank it - this slows down with a lot of hands. Poker makes this easier, by first sorting hands into types, and than you only have to compare hands within each type.
* Day 8: linked list