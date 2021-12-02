with open("i2.txt") as f:
    data = [x.replace("\n","") for x in f.readlines()]

position = {"horizontal": 0, "depth": 0, "aim": 0}

for x in data:
    command = x.split(" ")
    if(command[0] == "forward"):
        position["horizontal"] += int(command[1])
        position["depth"] += position["aim"] * int(command[1])
    elif(command[0] == "up"):
        position["aim"] -= int(command[1])
    elif(command[0] == "down"):
        position["aim"] += int(command[1])

print(f"Answer: {position['horizontal'] * position['depth']}")