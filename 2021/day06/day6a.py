with open("i6.txt") as f:
    fishes = [int(x) for x in f.read().strip().split(",")]

for day in range(80):
    new_fishes = []
    for f in range(len(fishes)):
        if fishes[f] > 0:
            fishes[f] -= 1
        elif fishes[f] == 0:
            new_fishes.append(8)
            fishes[f] = 6
    fishes += new_fishes

print(f"Result: {len(fishes)}")