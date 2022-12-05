import re

with open("2022/day05/input.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

sliced = []
curs = 0
while True:
    if lines[curs] == "":
        curs += 1
        break
    sliced.append([lines[curs][0:3].strip().replace("[", "").replace("]", "")] + [lines[curs][x:x+4].strip().replace("[", "").replace("]", "") for x in range(4, len(lines[curs]), 4)])
    curs += 1

stacks = []
for x in range(len(sliced[0])):
    stacks.append([sliced[y][x] for y in range(len(sliced)-2, -1, -1) if sliced[y][x]!=""])

for l in range(curs, len(lines)):
    x = re.match(r"move (\d+) from (\d+) to (\d+)", lines[l])
    moves = int(x.group(1))
    source = int(x.group(2))
    destination = int(x.group(3))

    for _ in range(moves):
        stacks[destination-1].append(stacks[source-1].pop(len(stacks[source-1])-1))

print("".join([x[len(x)-1] for x in stacks]))