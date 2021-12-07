def move_crab(a, b, mem):
    if (a, b) in fuel_memory.keys() or (b, a) in mem.keys():
        return mem[(a, b)]
    else:
        curr_fuel = 0
        for step in range(min(a, b) + 1, max(a, b) + 1):
            curr_fuel += step - min(a, b)
            
        mem[(a, b)] = curr_fuel
        mem[(b, a)] = curr_fuel
        return curr_fuel

with open("i7.txt") as f: data = [int(x) for x in f.read().strip().split(",")]

fuel_memory = dict()
min_fuel = -1
true_pos = 0
for pos in range(max(data) + 1):
    fuels = [move_crab(pos, x, fuel_memory) for x in data]
    
    fuel = sum(i for i in fuels)

    if (min_fuel == -1 or fuel < min_fuel):
        min_fuel = fuel
        true_pos = pos

print(f"Position: {true_pos}, Fuel: {min_fuel}")