with open("2022/day03/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

letters = []
for line in lines:
    left = set(line[0:int(len(line)/2)])
    right = set(line[int(len(line)/2):])
    letters += [x for x in left if x in right]


value_map = {}
for x in range(1, 27):
    value_map[chr(x+96)] = x
for x in range(27, 53):
    value_map[chr(x+38)] = x

result = 0
for l in letters:
    result += value_map[l]

print(result)

letters = []
line = 0
while line < len(lines):
    first = set(lines[line])
    second = set(lines[line+1])
    third = set(lines[line+2])
    letters += [x for x in first if x in second and x in third]
    line+=3

result = 0
for l in letters:
    result += value_map[l]

print(result)