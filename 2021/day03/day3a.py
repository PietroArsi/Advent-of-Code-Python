import math

with open("i3.txt") as f:
    data = [x.replace("\n", "") for x in f.readlines()]

input_length = len(data)
input_threshold = math.ceil(input_length / 2)
word_length = len(data[0])

gamma = [0 for x in range(word_length)]
epsilon = [1 for x in range(word_length)]

for bit in range(word_length):
    one_count = 0
    is_one=False
    for word in range(input_length):
        if (one_count > input_threshold):
            is_one = True
            break
        if(word_length - one_count > input_threshold):
            is_one = False
            break
        if (data[word][bit] == '1'):
            one_count += 1
    if(is_one):
        gamma[bit] = 1
        epsilon[bit] = 0

print(f"Gamma: {''.join([str(x) for x in gamma])}, Epsilon: {''.join([str(x) for x in epsilon])}, Power: {int(''.join([str(x) for x in gamma]), 2) * int(''.join([str(x) for x in epsilon]), 2)}")