from math import floor

with open("i6.txt") as f:
    data = [int(x) for x in f.read().strip().split(",")]

fishes = dict()
for x in range(9):
    fishes[x] = len([i for i in data if i == x])

simulation_days = 256
for day in range(simulation_days):
    newfishes = dict()
    for x in range(6): newfishes[x] = int(fishes[x+1])
    newfishes[6] = int(fishes[7]) + int(fishes[0])
    newfishes[7] = int(fishes[8])
    newfishes[8] = int(fishes[0])
    fishes = newfishes

count=0
for x in fishes.keys():
    count += fishes[x]

print(f"Result: {count}")