import math

with open("i3.txt") as f:
    data = [x.replace("\n", "") for x in f.readlines()]

input_length = len(data)
input_threshold = math.ceil(input_length / 2)
word_length = len(data[0])

words = [x for x in data]
for bit in range(word_length):
    one_count = 0
    ones = []
    zeroes = []
    for word in range(len(words)):
        if (words[word][bit] == '1'):
            ones.append(words[word])
            one_count += 1
        else:
            zeroes.append(words[word])
    
    if (one_count >= len(words)/2):
        words = [x for x in ones]
    else:
        words = [x for x in zeroes]
    ones.clear()
    zeroes.clear()
    one_count = 0
    # print(words)

    if(len(words) == 1):
        break

oxygen = words[0]

words = [x for x in data]
for bit in range(word_length):
    one_count = 0
    ones = []
    zeroes = []
    for word in range(len(words)):
        if (words[word][bit] == '1'):
            ones.append(words[word])
            one_count += 1
        else:
            zeroes.append(words[word])

    if (one_count < len(words)/2):
        words = [x for x in ones]
    else:
        words = [x for x in zeroes]
    ones.clear()
    zeroes.clear()
    one_count = 0
    if(len(words) == 1):
        break

co2 = words[0]

print(f"Oxygen: {oxygen}, CO2: {co2}, Power: {int(oxygen, 2) * int(co2, 2)}")