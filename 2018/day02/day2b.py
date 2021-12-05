from collections import defaultdict

with open('i2.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

found = False
result = ""
for i1 in data:
    for i2 in data:
        strike = 0
        strike_pos = -1
        for i in range(len(i1)):
            if i1[i] != i2[i]:
                strike += 1
                strike_pos = i
            if(strike > 1):
                break
        if(strike == 1):
            found = True
            result = i1[:strike_pos] + i1[strike_pos+1:]
            print(f"{i1} {i2}")
            break
    if found:
        break

print(f"Result: {result}")