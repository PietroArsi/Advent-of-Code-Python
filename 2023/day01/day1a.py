with open("2023/day01/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

total = 0
for line in lines:
    digits = []
    for c in line:
        try:
            d = int(c)
            digits.append(d)
        except:
            continue

    #print(digits[0] * 10 + digits[len(digits) - 1])
    total += digits[0] * 10 + digits[len(digits) - 1]

print(f"Total: {total}")