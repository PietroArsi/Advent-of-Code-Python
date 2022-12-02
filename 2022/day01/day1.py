import functools

with open("2022/day01/input.txt") as f:
    lines_raw = f.read()

calories = [functools.reduce(lambda a,b:a+b, [int(y) for y in x.split("\n")]) for x in lines_raw.split("\n\n")]
calories.sort(reverse=True)

print(f"Calories: {calories[0] + calories[1] + calories[2]}")