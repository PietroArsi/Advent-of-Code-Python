import json

with open("i8.txt") as f: data = [[y.strip().split() for y in x.strip().split("|")] for x in f.readlines()]
with open("mapping.json") as f: mapping = json.load(f)

def len2digit(l):
    for digit in mapping.keys():
        if l == mapping[digit]["length"]: return int(digit)

count=0
for x in data:
    for y in x[1]:
        if len2digit(len(y)) in [1, 4, 7, 8]:
            # print(f"{y} -> {len2digit(len(y))}")
            count += 1

print(f"Result: {count}")