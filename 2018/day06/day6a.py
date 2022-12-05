import string
from collections import defaultdict

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

with open("test.txt") as f:
    data = [[int(y) for y in x.strip().split(", ")] for x in f.readlines()]

points = dict()
for x in range(len(data)):
    points[string.ascii_lowercase[x]] = (data[x][0], data[x][1])

min_x = min(x[0] for x in data)
max_x = max(x[0] for x in data)
min_y = min(x[1] for x in data)
max_y = max(x[1] for x in data)

areas = defaultdict(int)

print(f"min_x: {min_x}, max_x: {max_x}, min_y: {min_y}, max_y: {max_y}")

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        ...