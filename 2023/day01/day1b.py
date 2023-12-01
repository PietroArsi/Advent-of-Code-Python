import re

with open("2023/day01/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

numbers = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

total = 0
for line in lines:
    digits = []

    position = 0
    current_substring = str(line)

    for x in range(len(line)):
        try:
            d = int(current_substring[0])
            #print(f"Matched {d}!")
            digits.append(d)
        except:
            for number in list(numbers.keys()):
                trimmed = current_substring[0:len(number)]
                if trimmed == number:
                    #print(f"Matched {number}!")
                    digits.append(numbers[trimmed])
        current_substring = current_substring[1:]

    total += digits[0] * 10 + digits[len(digits) - 1]

print(f"Total: {total}")