easy_test = 'aabcdefgaa'
hard_test = 'ieodomkazucvgmuy'

found = False
positions = []
for i, c in enumerate(list(hard_test)):
    if i < len(hard_test)-1:
        if len(positions) > 0:
            for p in positions:
                if [c, hard_test[i + 1]] == p[0] and i != p[1][1]:
                    found = True
        positions.append([[c, hard_test[i + 1]], [i, i+1]])
        
if found:
    print('Passed hard test')



# [['q','j'], [0, 1]]
        


