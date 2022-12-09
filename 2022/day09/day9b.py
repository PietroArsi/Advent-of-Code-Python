import re

with open("2022/day09/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

positions = set()

# head = (0,0)
rope = [(0,0) for x in range(10)]

for instruction in lines:
    amount = int(re.match(r"^\w (\d+)$", instruction).group(1))
    # print(amount)
    
    for step in range(amount):
        # print(f"{instruction[0]} {step}")
        if instruction[0] == "U":
            rope[0] = (rope[0][0], rope[0][1]+1)
        elif instruction[0] == "R":
            rope[0] = (rope[0][0]+1, rope[0][1])
        elif instruction[0] == "D":
            rope[0] = (rope[0][0], rope[0][1]-1)
        elif instruction[0] == "L":
            rope[0] = (rope[0][0]-1, rope[0][1])
        
        for x in range(0, 9):
            if rope[x][0] - rope[x+1][0] > 1:
                rope[x+1] = (rope[x+1][0]+1, rope[x+1][1])
                if rope[x][1] > rope[x+1][1]:
                    rope[x+1] = (rope[x+1][0], rope[x+1][1]+1)
                elif rope[x][1] < rope[x+1][1]:
                    rope[x+1] = (rope[x+1][0], rope[x+1][1]-1)

            elif rope[x][0] - rope[x+1][0] < -1:
                rope[x+1] = (rope[x+1][0]-1, rope[x+1][1])
                if rope[x][1] > rope[x+1][1]:
                    rope[x+1] = (rope[x+1][0], rope[x+1][1]+1)
                elif rope[x][1] < rope[x+1][1]:
                    rope[x+1] = (rope[x+1][0], rope[x+1][1]-1)

            elif rope[x][1] - rope[x+1][1] > 1:
                rope[x+1] = (rope[x+1][0], rope[x+1][1]+1)
                if rope[x][0] > rope[x+1][0]:
                    rope[x+1] = (rope[x+1][0]+1, rope[x+1][1])
                elif rope[x][0] < rope[x+1][0]:
                    rope[x+1] = (rope[x+1][0]-1, rope[x+1][1])
                    
            elif rope[x][1] - rope[x+1][1] < -1:
                rope[x+1] = (rope[x+1][0], rope[x+1][1]-1)
                if rope[x][0] > rope[x+1][0]:
                    rope[x+1] = (rope[x+1][0]+1, rope[x+1][1])
                elif rope[x][0] < rope[x+1][0]:
                    rope[x+1] = (rope[x+1][0]-1, rope[x+1][1])
        # print(f"{head} {tail}")
        positions.add(rope[9])
    # print("")

    # print(rope)
    # for b in range(40):
    #     for a in range(40):
    #         if (a-20,b-20) == rope[0]:
    #             print("H", end="")
    #         elif (a-20,b-20) == rope[1]:
    #             print("1", end="")
    #         elif (a-20,b-20) == rope[2]:
    #             print("2", end="")
    #         elif (a-20,b-20) == rope[3]:
    #             print("3", end="")
    #         elif (a-20,b-20) == rope[4]:
    #             print("4", end="")
    #         elif (a-20,b-20) == rope[5]:
    #             print("5", end="")
    #         elif (a-20,b-20) == rope[6]:
    #             print("6", end="")
    #         elif (a-20,b-20) == rope[7]:
    #             print("7", end="")
    #         elif (a-20,b-20) == rope[8]:
    #             print("8", end="")
    #         elif (a-20,b-20) == rope[9]:
    #             print("9", end="")
    #         elif (a-20,b-20) == (0,0):
    #             print("s", end="")
    #         else:
    #             print(".", end="")
    #     print("")
    # print("\n")

print(len(positions))