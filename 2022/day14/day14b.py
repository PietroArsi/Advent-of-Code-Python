import re

def printmap(rocks, s):
    f = open("2022/day14/out.txt", "a", encoding="utf-8")
    for y in range(0, 12):
        for x in range(470, 520):
            if y == 0 and x == 500:
                f.write("+")
            elif x in rocks.keys() and y in rocks[x]:
                f.write("#")
            elif x in s.keys() and y in s[x]:
                f.write("o")
            else:
                f.write(".")
        f.write("\n")
    f.write("\n")
    f.close()

with open("2022/day14/input.txt", encoding="utf-8") as f:
    lines = [x.strip() for x in f.readlines()]

coords = []
for l in lines:
    m = re.findall(r"(\d+),(\d+)", l)
    coords.append([(int(x[0]), int(x[1])) for x in m])

lowest = None
rockmap = dict()

for c in coords:
    for x in range(0, len(c)-1):
        if lowest == None or c[x][1] > lowest:
            lowest = c[x][1]
        
        # print(c[x])
        if c[x][0] == c[x+1][0]:
            b = max(c[x][1], c[x+1][1])
            a = min(c[x][1], c[x+1][1])
            for y in range(a, b+1):
                if c[x][0] not in set(rockmap.keys()):
                    rockmap[c[x][0]] = set()
                rockmap[c[x][0]].add(y)
        elif c[x][1] == c[x+1][1]:
            b = max(c[x][0], c[x+1][0])
            a = min(c[x][0], c[x+1][0])
            for y in range(a, b+1):
                if y not in set(rockmap.keys()):
                    rockmap[y] = set()
                rockmap[y].add(c[x][1])
        else:
            print("ERROR")

# f = open("2022/day14/out.txt", "w")
# f.close()

lowest += 2

sands = dict()
count = 0

total_map = {k: rockmap.get(k, set()).union(sands.get(k, set())) for k in set(rockmap.keys()).union(set(sands.keys()))}

while True:
    sand = (500,0)
    # printmap(rockmap, sands)

    exit = False
    print(count)
    while True:
        # total_map = {k: rockmap.get(k, set()).union(sands.get(k, set())) for k in set(rockmap.keys()).union(set(sands.keys()))}

        if sand[1] == lowest-1:
            count += 1
            # if sand[0] not in set(sands.keys()):
            #     sands[sand[0]] = set()
            if sand[0] not in set(total_map.keys()):
                total_map[sand[0]] = set()
            total_map[sand[0]].add(sand[1])
            # sands[sand[0]].add(sand[1])
            break
        elif sand[0] not in set(total_map.keys()) or sand[1]+1 not in total_map[sand[0]]:
            sand = (sand[0], sand[1]+1)
        elif sand[0]-1 not in set(total_map.keys()) or sand[1]+1 not in total_map[sand[0]-1]:
            sand = (sand[0]-1, sand[1]+1)
        elif sand[0]+1 not in set(total_map.keys()) or sand[1]+1 not in total_map[sand[0]+1]:
            sand = (sand[0]+1, sand[1]+1)
        else:
            count += 1

            # if sand[0] not in set(sands.keys()):
            #     sands[sand[0]] = set()
            if sand[0] not in set(total_map.keys()):
                total_map[sand[0]] = set()
            total_map[sand[0]].add(sand[1])
            # sands[sand[0]].add(sand[1])

            if sand == (500,0):
                exit = True
            break
    if exit:
        break

print(count)