with open("i1.txt", "r") as f:
    data = [int(x) for x in f.readlines()]
    
data = [data[x] for x in range(len(data))]

incr=0
for x in range(1, len(data)):
    if(data[x] > data[x-1]):
        incr += 1

print(f"Part 1: {incr}")