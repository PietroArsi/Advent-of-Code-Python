import re

regex = r"^#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)$"

with open("i3.txt") as f:
    data = [x.strip() for x in f.readlines()]

claimed = set()
multi_claimed = set()
more_than_one = 0

for line in data:
    x = re.search(regex, line)
    if x:
        eid = int(x.group(1))
        xc = int(x.group(2))
        yc = int(x.group(3))
        w = int(x.group(4))
        h = int(x.group(5))
        for i in range(xc, xc + w):
            for j in range(yc, yc + h):
                if (i, j) in claimed:
                    multi_claimed.add((i, j))
                else:
                    claimed.add((i, j))

print(f"Result: {len(multi_claimed)}")