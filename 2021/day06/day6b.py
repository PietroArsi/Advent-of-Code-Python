with open("i6.txt") as f: data = [int(x) for x in f.read().strip().split(",")]

fishes = {val:data.count(val) for val in range(9)}

print(fishes)

simulation_days = 256
for day in range(simulation_days):
    newfishes = dict()
    for x in range(6): newfishes[x] = int(fishes[x+1])
    newfishes[6] = int(fishes[7]) + int(fishes[0])
    newfishes[7] = int(fishes[8])
    newfishes[8] = int(fishes[0])
    fishes = newfishes

print(f"Result: {sum(i for i in fishes.values())}")