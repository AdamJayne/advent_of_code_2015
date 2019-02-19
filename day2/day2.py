

puzzle = open('puzzle.txt', 'r').read().split("\n")

tupled = []
surface_area_total = 0
ribbon_length = 0

for x in puzzle:
   chunked = x.split('x')
   tupled.append((int(chunked[0]), int(chunked[1]), int(chunked[2])))

for x in tupled:
    srt = [z for z in x]
    srt.sort()
    smallest = srt[0] * srt[1]
    surface_area_total += (2*x[0]*x[1]) + (2*x[1]*x[2]) + (2*x[2]*x[0])
    surface_area_total += smallest

    ribbon = (2*srt[0] + 2*srt[1]) + (srt[0] * srt[1] * srt[2])
    ribbon_length += ribbon

print(surface_area_total)
print(ribbon_length)


