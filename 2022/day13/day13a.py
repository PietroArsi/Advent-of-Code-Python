import functools

def is_lower(arg1, arg2):
    # print(f"{arg1} < {arg2} ? ")
    if isinstance(arg1, int) and isinstance(arg2, int):
        if arg1 < arg2:
            return -1
        elif arg1 == arg2:
            return 0
        elif arg1 > arg2:
            return 1
    elif isinstance(arg1, int) and isinstance(arg2, list):
        return is_lower([arg1], arg2)
    elif isinstance(arg1, list) and isinstance(arg2, int):
        return is_lower(arg1, [arg2])
    else:
        c = 0
        while c < max(len(arg1), len(arg2)):
            try:
                param1 = arg1[c]
            except IndexError as exc:
                return -1
            try:
                param2 = arg2[c]
            except IndexError as exc:
                return 1

            check = is_lower(param1, param2)

            if check == -1:
                return -1
            elif check == 0:
                pass
            elif check == 1:
                return 1
            c += 1

with open("2022/day13/input.txt", encoding="utf-8") as f:
    lines = [[eval(y) for y in x.strip().split("\n")] for x in f.read().split("\n\n")]

indexes = []

for curs in range(len(lines)):
    if is_lower(lines[curs][0], lines[curs][1]) == -1:
        indexes.append(curs+1)
    curs += 1

print(f"Result: {functools.reduce(lambda a,b:a+b, indexes)}")