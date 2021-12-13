from collections import defaultdict

def print_manual(x_dim, y_dim, m):
    for y in range(y_dim + 1):
        for x in range(x_dim + 1):
            if (x, y) in m:
                print("#", end="")
            else:
                print(".", end="")
        print()

with open("i13.txt") as f: data = [x.strip() for x in f.readlines()]

points = list()
instructions = list()
for x in data:
    if x == "":
        continue
    if x[0] == "f":
        instructions.append(x)
    else:
        points.append(x)

x_dim = 0
y_dim = 0

points_yx = defaultdict(list)
points_xy = defaultdict(list)
map = set()

for x in points:
    t = x.split(',')

    points_yx[int(t[1])].append(int(t[0]))
    points_xy[int(t[0])].append(int(t[1]))
    map.add((int(t[0]), int(t[1])))

    if int(t[0]) > x_dim:
        x_dim = int(t[0])
    if int(t[1]) > y_dim:
        y_dim = int(t[1])

# print_manual(x_dim, y_dim, map)
print("")

for i in instructions:
    t = i.split('=')
    folding_point = int(t[1])
    if t[0][-1] == "x":
        new_map = set()
        for p in map:
            # print(f"{p} -> {p[0]},{folding_point - (p[1] - folding_point)}")
            if p[0] > folding_point:
                new_map.add((folding_point - (p[0] - folding_point), p[1]))
            else:
                new_map.add((p[0], p[1]))
        map = new_map
        x_dim = folding_point - 1
    elif t[0][-1] == "y":
        new_map = set()
        for p in map:
            # print(f"{p} -> {p[0]},{folding_point - (p[1] - folding_point)}")
            if p[1] > folding_point:
                new_map.add((p[0], folding_point - (p[1] - folding_point)))
            else:
                new_map.add((p[0], p[1]))
        map = new_map
        y_dim = folding_point - 1
    
    break

# print_manual(x_dim, y_dim, map)

print(f"Points: {len(map)}")