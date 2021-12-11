from collections import defaultdict

with open("i11.txt") as f: map = [[int(y) for y in list(x.strip())] for x in f.readlines()]

def flash(a, b, m, check):
    check[b][a] = True
    x_dim = len(m[0])
    y_dim = len(m)

    count = 1
    if a > 0:
        m[b][a-1] += 1
        if m[b][a-1] > 9 and not check[b][a-1]:
            count += flash(a-1, b, m, check)
    if a > 0 and b > 0:
        m[b-1][a-1] += 1
        if m[b-1][a-1] > 9 and not check[b-1][a-1]:
            count += flash(a-1, b-1, m, check)
    if b > 0:
        m[b-1][a] += 1
        if m[b-1][a] > 9 and not check[b-1][a]:
            count += flash(a, b-1, m, check)
    if b > 0 and a < x_dim-1:
        m[b-1][a+1] += 1
        if m[b-1][a+1] > 9 and not check[b-1][a+1]:
            count += flash(a+1, b-1, m, check)
    if a < x_dim-1:
        m[b][a+1] += 1
        if m[b][a+1] > 9 and not check[b][a+1]:
            count += flash(a+1, b, m, check)
    if a < x_dim-1 and b < y_dim-1:
        m[b+1][a+1] += 1
        if m[b+1][a+1] > 9 and not check[b+1][a+1]:
            count += flash(a+1, b+1, m, check)
    if b < y_dim-1:
        m[b+1][a] += 1
        if m[b+1][a] > 9 and not check[b+1][a]:
            count += flash(a, b+1, m, check)
    if b < y_dim-1 and a > 0:
        m[b+1][a-1] += 1
        if m[b+1][a-1] > 9 and not check[b+1][a-1]:
            count += flash(a-1, b+1, m, check)
    
    return count

days_passed = 0
all_flashing = False
flash_day = -1
while not all_flashing:
    flashed = [[False for x in range(len(map[0]))] for y in range(len(map))]
    # octos = defaultdict(list)

    flashing = []

    for y in range(len(map)):
        for x in range(len(map[y])):
            map[y][x] += 1
            if map[y][x] > 9:
                flashing.append((x, y))
    
    # print(flashing)
    count = 0
    for t in flashing:
        if not flashed[t[1]][t[0]]:
            count += flash(t[0], t[1], map, flashed)
    
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] > 9:
                map[y][x] = 0

    days_passed += 1

    if count == sum(1 for y in map for x in y):
        flash_day = days_passed
        all_flashing = True

    # print(f"Day {d+1}")
    # for x in map:
    #     print(f"{''.join([str(y).rjust(3) for y in x])}")
    # print("")
    
        
print(f"Flash day: {flash_day}")