puzzle = list(open('puzzle.txt', 'r').read())


class Santa:
    """
        Santa class to track position and previous movements
    """
    def __init__(self):
        self.position = [0, 0]
        self.visited_houses = [[0, 0]]

    def move(self, instruction):
        if instruction == '^':
            self.position[1] += 1
        elif instruction == '>':
            self.position[0] += 1
        elif instruction == 'v':
            self.position[1] -= 1
        elif instruction == '<':
            self.position[0] -= 1
        self.visited_houses.append(self.position[:])


# First santa instance
santa = Santa()

# Execute santa's first instruction set
for instruction in puzzle:
    santa.move(instruction)

# Prep for checking unique houses
unique_houses = []

# Unique house logic
for house in santa.visited_houses:
    if house not in unique_houses:
        unique_houses.append(house)

print(len(unique_houses))

# ===============
# PART 2

santa_list = []
bot_list = []

# Creates instances for santa and his bot
santa2 = Santa()
bot = Santa()

# Splits the commands into santa's movements, and the bot's
for i, instruction in enumerate(puzzle):
    if i % 2 == 0:
        santa_list.append(instruction)
    else:
        bot_list.append(instruction)

# Execute santa's instructions
for instruction in santa_list:
    santa2.move(instruction)

# Execute bot's instructions
for instruction in bot_list:
    bot.move(instruction)

# Prep for checking unique houses
unique2 = []

for house in santa2.visited_houses:
    if house not in unique2:
        unique2.append(house)

for house in bot.visited_houses:
    if house not in unique2:
        unique2.append(house)

print(len(unique2))


