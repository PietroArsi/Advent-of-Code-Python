from collections import defaultdict

with open('i2.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

twice = 0
thrice = 0
for ID in data:
    counts = defaultdict(int)
    for c in ID:
        counts[c] += 1
    
    found_twice = False
    found_thrice = False
    for c in counts.keys():
        if counts[c] == 2 and not found_twice:
            found_twice = True
            twice += 1
        elif counts[c] == 3 and not found_thrice:
            found_thrice = True
            thrice += 1

print(f"Result: {twice * thrice}")