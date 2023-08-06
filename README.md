# Advent of Code 2022
My late attemps at solutions for Advent of Code from 2022, trying my best not to cheat.

## Day 1
> `python`

For part 1, I iterated over arrays and kept track of the current maximum calorie total. For part 2, built an array of all elves' calorie totals, then sorted and took the sum of the last 3 (highest) values.


## Day 2
> `python`

First, I defined the scores for shape and duel results. We are given the scores for the shapes in the first task explicitly, and we must define the scores for each possible duel. In the second task, the opposite is true. We are explicitly told how duels will turn out, and we have to determine the appropriate shape to play.

Then I wrote two functions for evaluating the score for single line of the input (round). Note, that input_line[2] represents the last letter of input line (shape in the first task, and duel outcome in the second one) and input_line[:3] represents the whole input line (duel outcome in the first task, and shape in the second task).

Finally there is the solution function which opens the input file in read mode and sums scores from all of the rounds in a list comprehension using evaluate_function_task_n function.

## Day 3
> python

1. split data lines in halves, set priorities and added them up
2. grouped sets into 3s and found sum

## Day 4
> python

things