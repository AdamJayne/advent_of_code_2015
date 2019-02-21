puzzle = open('puzzle.txt').read().split('\n')

vowels = ['a', 'e', 'i', 'o', 'u']
bad = ['ab', 'cd', 'pq', 'xy']
nice_strings = 0
nice_strings_2 = 0

# Part 1
for s in puzzle:
    no_bad = True
    found_double = False
    vowel_count = 0
    chars = list(s)
    for i, c in enumerate(chars):
        if c in vowels:
            vowel_count += 1
        if i < len(chars)-1:
            for z in bad:
                if c + chars[i+1] == z:
                    no_bad = False 
        if i < len(chars)-1 and c == chars[i+1]:
            found_double = True
    if no_bad and found_double and vowel_count >= 3:
        nice_strings += 1

print(nice_strings)


# Part 2
for s in puzzle:
    found_repeat = False
    found_dub = False
    positions = []
    chars = list(s)
    for i, c in enumerate(chars):
        if i > 1 and c == chars[i - 2]:
            found_repeat = True
        if i < len(chars)-1:
            if len(positions) > 0:
                for p in positions:
                    if [c, chars[i+1]] == p[0] and i != p[1][1]:
                        found_dub = True
            positions.append([[c, chars[i+1]], [i, i+1]])

    if found_repeat and found_dub:
        nice_strings_2 += 1
print(nice_strings_2)

        
