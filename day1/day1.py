puzzle = open('puzzle.txt', 'r').read()


puzzle = list(puzzle)
floor = 0
in_basement = False

for i, val in enumerate(puzzle):
    if val == "(":
        floor += 1
    elif val == ")":
        floor -= 1
    if not in_basement:
        if floor == -1:
            in_basement = True
            print('Hit basement at position:', i + 1)


print(floor)
