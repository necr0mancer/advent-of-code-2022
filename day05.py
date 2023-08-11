from string import ascii_uppercase

with open("05data.txt") as inputfile:
    #data = [i for i in inputfile.read().strip().split("\n").split("\n\n")]
    stack_list, instruct = (i.splitlines() for i in inputfile.read().strip("\n").split("\n\n"))
    
    #print(stack_list, "\n\n", instruct)

"""
'stacks' is a dictionary that will store {stack number}:{[characters in stack]}
'indexes' is a list that stores the indexes in which the characters needed to fill 
    the stacks will be found. 
"""

stacks = {int(digit):[] for digit in stack_list[-1].replace(" ","")}
indexes = [index for index, char in enumerate(stack_list[-1]) if char != " "]

# Used to display the contents in each stack
def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")

# Loading the stacks off the input
def loadStacks():
    for string in stack_list[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] == " ":
                pass
            else:
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

# Clearing the lists in every stack
def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

def getStackEnds():
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer

loadStacks()

# Strip "words" from instruction set
for step in instruct:
    step = step.replace("move ", "").replace("from ", "").replace("to ", "").strip().split(" ")
    step = [int(i) for i in step]
    # print(step)
    # Set variables for each value
    crates = step[0]
    from_stack = step[1]
    to_stack = step[2]
# Select crate [0] from range, remove from stack [1] and append to new home [2]
    for crate in range(crates):
        #move [1] to [2]
        removed = stacks[from_stack].pop()
        stacks[to_stack].append(removed)





print("Answer: ", getStackEnds())