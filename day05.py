with open("05data.txt") as inputfile:
    #data = [i for i in inputfile.read().strip().split("\n").split("\n\n")]
    stack_list, instructions = (i.splitlines() for i in inputfile.read().strip("\n").split("\n\n"))
    
    print(stack_list, "\n\n", instructions)

