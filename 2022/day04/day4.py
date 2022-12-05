with open("2022/day04/input.txt") as f:
    lines = [[y for y in x.strip().split(",")] for x in f.readlines()]

count = 0
for l in lines:
    first = [x for x in range(int(l[0].split("-")[0]), int(l[0].split("-")[1]) + 1)]
    second = [x for x in range(int(l[1].split("-")[0]), int(l[1].split("-")[1]) + 1)]
    
    if set(first).issubset(set(second)) or set(second).issubset(set(first)):
        count += 1

print(count)

count = 0
for l in lines:
    first = [x for x in range(int(l[0].split("-")[0]), int(l[0].split("-")[1]) + 1)]
    second = [x for x in range(int(l[1].split("-")[0]), int(l[1].split("-")[1]) + 1)]
    
    if len(set(first).intersection(set(second))) > 0:
        count += 1

print(count)