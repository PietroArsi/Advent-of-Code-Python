with open('i1.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

frequency = 0
frequency_set = set()
frequency_set.add(frequency)
found = False
while(not found):
    for line in range(len(data)):
        if(data[line][0] == '+'):
            frequency += int(data[line][1:])
        else:
            frequency -= int(data[line][1:])

        if(frequency in frequency_set):
            print(f"Frequency: {frequency}")
            found = True
            break
        else:
            frequency_set.add(frequency)