# adventofcode2016

Python solutions for Advent of Code 2016 - http://adventofcode.com/2016

> Advent of Code is a series of small programming puzzles for a variety of skill levels. They are self-contained and are just as appropriate for an expert who wants to stay sharp as they are for a beginner who is just learning to code. Each puzzle calls upon different skills and has two parts that build on a theme.

This repo contains a jupyter notebook for each day. The solutions are all a bit verbose as I'm trying to show all the steps I'm taking to solve the puzzles.

# Notes

## Day 1

I found the simple things like turning directions tougher than the bigger problem. So doing it in pieces really helped.



# notes on each puzzle:

Day    | Kind of Problem | Notes
------ | --------------- | -----
Day 1  | Path | I found the simple things like turning directions tougher than the bigger problem. So doing it in pieces really helped.
Day 2 | move around a numpad | used both numpy and lists. Key takeaway: use a char to demarcate edges
Day 3 | simple math and slicing a grid | numpy for the win, basically use numpy if there is anything like a grid to deal with. 
Day 4 | ? | use Counter and namedtuples
Day 5 | find a password | used hashlib, was an interesting problem
Day 6  | Path | I found the simple things like turning directions tougher than the bigger problem. So doing it in pieces really helped.
Day 7 | move around a numpad | used both numpy and lists. Key takeaway: use a char to demarcate edges
Day 8 | simple math and slicing a grid | numpy for the win, basically use numpy if there is anything like a grid to deal with. 
Day 9 | ? | use Counter and namedtuples
Day 10  | parsing instructions | was a challange to fully comprehend the problem, though easy to code.
Day 11 | building the right kind of graph with breadth first search | solved part 1 using a dumb BFS, but part two the search space is so big that I need to optimize. #TODO
Day 12 | parse instructions to update registers | sort of like building a vm?
Day 13 | build a map and find a path | used bfs, easy enough, but need to implement a generic path solver. its got pics too!
Day 14 | find a password | used hashlib, was an interesting problem
Day 15 | solve a system | find positions of a moving system at time t. Could have used math instead.
Day 16 | find a password | used hashlib, was an interesting problem
Day 17 | Get shortest, than longest path | looked similar to day 13, but different. 


## Day 22: Grid Computing

get all the numbers from a string:

```python
[int(i) for i in re.findall('\d+', line)]
```

## General takeaways

regex's can make hard things easy at the cost of the regex itself being hard. luckily there are lots great regex sites.



- dispatch tables are great
- write little functions. Some of the problems seemed very hard, and I used the famous anti-procrastination advice of just start with the smallest thing you can do and lo and behold in the middle of writing the most basic two line function I would see how to write the next one, and the next, and soon enough the entire bigger problem was done
- little functions really help with being able to read the code and troubleshoot.
- many problems are just graphs, which can be implemented many ways, from using classes to lists to dicts. but its still all graphs.
- python has lots of great tools in libraries like `collections` which should just be in the language. why do I have to import things like `defaultdict` which it is so useful that it should be there in the first place
- implementing something myself makes it stick in my brain, vs googling a solution
- if/else in list comprehensions can be great: `"".join([c if c != False else "_" for c in password]`
- the algo matters more than the machine speed. I moved my Day 11 solution to a super beefy high memory machine to brute force the solution - but it was taking the same runtime as on a small 1gb mem shared server. The fault was with the overly slow code, not the machine speed.