from collections import defaultdict

with open("i14.txt") as f: lines = [x.strip() for x in f.readlines()]

formula = lines[0]
reactions = lines[2:]
reaction_table = dict()

for x in reactions:
    elements = x.split(" -> ")
    reaction_table[elements[0]] = elements[1]

steps = 10
for _ in range(steps):
    new_formula = ""
    flag = False
    for x in range(len(formula) - 1):
        a = formula[x]
        b = formula[x + 1]
        if not flag:
            new_formula += f"{a}{reaction_table[a+b]}{b}"
            flag = True
        else:
            new_formula += f"{reaction_table[a+b]}{b}"
        # formula = f"{formula[:x]}{reaction_table[a+b]}{formula[x:]}"
    formula = new_formula

counter = defaultdict(int)
for x in formula:
    counter[x] += 1

max_count = max(counter.values())
min_count = min(counter.values())

print(f"Result: {max_count - min_count}")