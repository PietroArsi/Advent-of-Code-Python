import string

with open("i5.txt") as f: data = [x.strip() for x in f.readlines()]

line = data[0]
units = list(line)

alphabet = list(string.ascii_lowercase)
values = dict()

for char in alphabet:
    x=0
    units_fixed = [c for c in units if c.lower() != char]
    while(x < len(units_fixed)-1):
        if units_fixed[x] != units_fixed[x+1] and (units_fixed[x].lower() == units_fixed[x+1].lower()):
            units_fixed.pop(x+1)
            units_fixed.pop(x)
            x -= 2
            if x < 0: x = 0
        else:
            x += 1
    values[char] = len(units_fixed)

min_value = min(list(values.values()))

print(min_value)