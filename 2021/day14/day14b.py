from collections import defaultdict

def react(polymer, table, step, limit):
    ...

with open("test14.txt") as f: lines = [x.strip() for x in f.readlines()]

formula = list(lines[0])
reactions = lines[2:]
reaction_table = dict()
counter = defaultdict(int)

for x in reactions:
    elements = x.split(" -> ")
    reaction_table[elements[0]]=dict()
    reaction_table[elements[0]][1] = elements[1]

counter[formula[0]] += 1
transformed_elements = list()
steps = 40
for x in range(len(formula) - 1):
    first = formula[x]
    second = formula[x + 1]
    counter[second] += 1

    print(f"Inspecting: {first} {second}")

    temp_formula = [first, second]

    max_known = max([i for i in reaction_table[first+second].keys() if i <= steps])
    print(f"I already know {max_known} steps for {first}{second}")
    temp_formula = temp_formula[:max_known]+list(reaction_table[first+second][max_known])+temp_formula[max_known:]
    
    cycle = max_known
    while cycle < steps:
        # per ogni ciclo che devo fare

        temp_formula2 = [temp_formula[0]]

        max_known2 = 1

        cycle2 = 0
        # for y in range(len(temp_formula) - 1):
        while cycle2 < len(temp_formula) - 1:
            a = temp_formula[cycle2]
            b = temp_formula[cycle2+1]

            temp_formula2 += reaction_table[a+b][max_known2]
            temp_formula2 += list(b)
            counter[reaction_table[a+b][1]] += 1

            cycle2 += 1

        if cycle+1 not in reaction_table[first+second].keys():
            reaction_table[first+second][cycle+1] = "".join(temp_formula2[1:len(temp_formula2)-1])
        temp_formula = list(temp_formula2)
        cycle += 1
    
    # print(f"{first} {second} -> {''.join(temp_formula)}")
    print("")

# print(reaction_table)

max_count = max(counter.values())
min_count = min(counter.values())

print(f"Result: {max_count - min_count}")