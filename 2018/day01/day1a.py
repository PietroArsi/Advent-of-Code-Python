with open('i1.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

frequency = 0
for line in input:
    if(line[0] == '+'):
        frequency += int(line[1:])
    else:
        frequency -= int(line[1:])

print(f"Frequency: {frequency}")