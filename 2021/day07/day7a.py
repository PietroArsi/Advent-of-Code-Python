with open("test7.txt") as f: data = [int(x) for x in f.read().strip().split(",")]

min_fuel = -1
true_pos = 0
for pos in range(max(data) + 1):
    fuels = [abs(i - pos) for i in data]
    # print(f"{pos}: {fuels}")
    fuel = sum(i for i in fuels)
    if (min_fuel == -1 or fuel < min_fuel):
        min_fuel = fuel
        true_pos = pos

print(f"Position: {true_pos}, Fuel: {min_fuel}")