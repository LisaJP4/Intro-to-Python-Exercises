def pipe_fix(input):
    mylist = []
    for x in range (input[0], input[len(input) - 1] +1):
        mylist.append(x)
    return mylist

input = 1, 2, 3, 5, 7, 9
print(pipe_fix(input))
