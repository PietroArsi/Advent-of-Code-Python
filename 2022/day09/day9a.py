import re

with open("2022/day09/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

positions = set()

head = (0,0)
tail = (0,0)

for instruction in lines:
    amount = int(re.match(r"^\w (\d+)$", instruction).group(1))
    # print(amount)
    
    for step in range(amount):
        # print(f"{instruction[0]} {step}")
        if instruction[0] == "U":
            head = (head[0], head[1]+1)
        elif instruction[0] == "R":
            head = (head[0]+1, head[1])
        elif instruction[0] == "D":
            head = (head[0], head[1]-1)
        elif instruction[0] == "L":
            head = (head[0]-1, head[1])
        
        if head[0] - tail[0] > 1:
            tail = (tail[0]+1, tail[1])
            if head[1] > tail [1]:
                tail = (tail[0], tail[1]+1)
            elif head[1] < tail [1]:
                tail = (tail[0], tail[1]-1)
        elif head[0] - tail[0] < -1:
            tail = (tail[0]-1, tail[1])
            if head[1] > tail [1]:
                tail = (tail[0], tail[1]+1)
            elif head[1] < tail [1]:
                tail = (tail[0], tail[1]-1)
        elif head[1] - tail[1] > 1:
            tail = (tail[0], tail[1]+1)
            if head[0] > tail [0]:
                tail = (tail[0]+1, tail[1])
            elif head[0] < tail [0]:
                tail = (tail[0]-1, tail[1])
        elif head[1] - tail[1] < -1:
            tail = (tail[0], tail[1]-1)
            if head[0] > tail [0]:
                tail = (tail[0]+1, tail[1])
            elif head[0] < tail [0]:
                tail = (tail[0]-1, tail[1])
        # print(f"{head} {tail}")
        positions.add(tail)
    # print("")

# print(positions)
print(len(positions))