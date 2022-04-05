import re

regex = r"^#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)$"

with open("i3.txt") as f:
    data = [x.strip() for x in f.readlines()]

claimed = dict()
multi_claimed = dict()
ids = list()

for line in data:
    x = re.search(regex, line)
    if x:
        eid = int(x.group(1))
        xc = int(x.group(2))
        yc = int(x.group(3))
        w = int(x.group(4))
        h = int(x.group(5))

        ids.append(int(eid))    

        for i in range(xc, xc + w):
            for j in range(yc, yc + h):
                if (i, j) in multi_claimed.keys():
                    banned = [int(eid)]
                    multi_claimed[(i, j)].append(eid)
                    ids = [x for x in ids if x not in banned]
                elif (i, j) not in multi_claimed.keys() and (i, j) in claimed.keys():
                    banned = [int(eid), int(claimed[(i, j)])]
                    multi_claimed[(i, j)] = [int(claimed[(i, j)])]
                    claimed.pop((i, j))
                    ids = [x for x in ids if x not in banned]
                elif (i, j) in claimed.keys() and eid not in claimed[(i, j)]:
                    claimed[(i, j)].append((i, j))
                elif eid not in claimed.keys():
                    claimed[(i, j)] = int(eid)

print(f"Result: {ids[0]}")