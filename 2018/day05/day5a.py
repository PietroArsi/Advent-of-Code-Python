

with open("i5.txt") as f: data = [x.strip() for x in f.readlines()]

line = data[0]
units = list(line)

# print("".join(units))

x=0
while(x < len(units)-1):
    if units[x] != units[x+1] and (units[x].lower() == units[x+1].lower()):
        units.pop(x+1)
        units.pop(x)
        x -= 2
        if x < 0: x = 0
    else:
        x += 1
    # print("".join(units))

print(len(units))