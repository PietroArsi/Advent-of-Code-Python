with open("i9.txt") as f: map = [[int(y) for y in x.strip()] for x in f.readlines()]

def is_low(a, b, mapt):
    x_dim = len(mapt[0])
    y_dim = len(mapt)
    if a == 0 or a > 0 and mapt[b][a] < mapt[b][a-1]:
        if b == 0 or b > 0 and mapt[b][a] < mapt[b-1][a]:
            if a == x_dim-1 or a < x_dim-1 and mapt[b][a] < mapt[b][a+1]:
                if b == y_dim-1 or b < y_dim-1 and mapt[b][a] < mapt[b+1][a]:
                    return True

def is_basin(a, b, mapt, bmap):
    x_dim = len(mapt[0])
    y_dim = len(mapt)
    count = 0
    if a > 0 and mapt[b][a-1] != 9 and bmap[b][a-1] == False:
        bmap[b][a-1] = True
        count += is_basin(a-1, b, mapt, bmap) + 1
    if b > 0 and mapt[b-1][a] != 9 and bmap[b-1][a] == False:
        bmap[b-1][a] = True
        count += is_basin(a, b-1, mapt, bmap) + 1
    if a < x_dim-1 and mapt[b][a+1] != 9 and bmap[b][a+1] == False:
        bmap[b][a+1] = True
        count += is_basin(a+1, b, mapt, bmap) + 1
    if b < y_dim-1 and mapt[b+1][a] != 9 and bmap[b+1][a] == False:
        bmap[b+1][a] = True
        count += is_basin(a, b+1, mapt, bmap) + 1
    return count

lowpoints = []
for y in range(len(map)):
    for x in range(len(map[y])):
        if is_low(x, y, map):
            lowpoints.append((int(x),int(y)))

areas = []
basinmap = [[False for x in range(len(map[0]))] for y in range(len(map))]
for point in lowpoints:
    basinmap[point[1]][point[0]] = True
    areas.append(int(is_basin(point[0], point[1], map, basinmap) + 1))

areas.sort(reverse=True)

print(f"Result: {areas[0] * areas[1] * areas[2]}")