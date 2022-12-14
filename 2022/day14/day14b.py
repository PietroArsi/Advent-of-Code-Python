import re

with open("2022/day14/input.txt", encoding="utf-8") as f:
    lines = [x.strip() for x in f.readlines()]

coords = []
for l in lines:
    m = re.findall(r"(\d+),(\d+)", l)
    coords.append([(int(x[0]), int(x[1])) for x in m])

# print(coords)
lowest = None
map = set()
for c in coords:
    for x in range(0, len(c)-1):
        if lowest == None or c[x][1] > lowest:
            lowest = c[x][1]
        
        # print(c[x])
        if c[x][0] == c[x+1][0]:
            b = max(c[x][1], c[x+1][1])
            a = min(c[x][1], c[x+1][1])
            for y in range(a, b+1):
                map.add((c[x][0], y))
        elif c[x][1] == c[x+1][1]:
            b = max(c[x][0], c[x+1][0])
            a = min(c[x][0], c[x+1][0])
            for y in range(a, b+1):
                map.add((y, c[x][1]))
        else:
            print("ERROR")

# print(lowest)
# print(map)

lowest += 2

sands = set()
count = 0
while True:
    sand = (500,0)

    exit = False
    print(count)
    while True:
        # print(sand)
        if sand[1] == lowest-1:
            count += 1
            sands.add(sand)
            break
        elif (sand[0], sand[1]+1) not in map.union(sands):
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in map.union(sands):
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in map.union(sands):
            sand = (sand[0]+1, sand[1]+1)
        else:
            count += 1
            sands.add(sand)
            if sand == (500,0):
                exit = True
            break
    if exit:
        break

print(count)