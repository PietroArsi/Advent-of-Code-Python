import json
from collections import defaultdict

with open("i8.txt") as f: data = [[y.strip().split() for y in x.strip().split("|")] for x in f.readlines()]
with open("mapping.json") as f: mapping = json.load(f)

def len2digit(l):
    result = []
    for digit in mapping.keys():
        if l == mapping[digit]["length"]: result.append(int(digit))
    if len(result) == 1: return result[0]
    else: return result

def get_digit(d, l):
    result = []
    for k in l:
        if len(k) == mapping[str(d)]["length"]:
            result.append(k)
    return result

def get_digit_by_len(length, l):
    result = []
    for k in l:
        if len(k) == length:
            result.append(k)
    return result

def reset(w):
    for x in w.keys():
        w[x] = list()

def fix_wiring(w):
    for k in w.keys():
        if len(w[k]) == 1:
            for i in w.keys():
                if(i != k and w[k][0] in w[i]):
                    w[i].remove(w[k][0])

def digit2int(code, w):
    display = {"up" : False, "up left": False, "up right": False, "center": False, "down left": False, "down right": False, "down": False}
    for d in w.keys():
        if w[d][0] in code:
            display[d] = True

    print(display)

    if display["up"] and display["up left"] and display["up right"] and not display["center"] and display["down left"] and display["down right"] and display["down"]:
        return 0
    elif not display["up"] and not display["up left"] and display["up right"] and not display["center"] and not display["down left"] and display["down right"] and not display["down"]:
        return 1
    elif display["up"] and not display["up left"] and display["up right"] and display["center"] and display["down left"] and not display["down right"] and display["down"]:
        return 2
    elif display["up"] and not display["up left"] and display["up right"] and display["center"] and not display["down left"] and display["down right"] and display["down"]:
        return 3
    elif not display["up"] and display["up left"] and display["up right"] and display["center"] and not display["down left"] and display["down right"] and not display["down"]:
        return 4
    elif display["up"] and display["up left"] and not display["up right"] and display["center"] and not display["down left"] and display["down right"] and display["down"]:
        return 5
    elif display["up"] and display["up left"] and not display["up right"] and display["center"] and display["down left"] and display["down right"] and display["down"]:
        return 6
    elif display["up"] and not display["up left"] and display["up right"] and not display["center"] and not display["down left"] and display["down right"] and not display["down"]:
        return 7
    elif display["up"] and display["up left"] and display["up right"] and display["center"] and display["down left"] and display["down right"] and display["down"]:
        return 8
    elif display["up"] and display["up left"] and display["up right"] and display["center"] and not display["down left"] and display["down right"] and display["down"]:
        return 9

wiring = {"up" : [], "up left": [], "up right": [], "center": [], "down left": [], "down right": [], "down": []}
wires = ["a", "b", "c", "d", "e", "f", "g"]

count=0
for x in data:
    reset(wiring)
    for y in x[0] + x[1]:
        digit = len2digit(len(y))
        letters = y.split()

    codes = defaultdict(list)
    digits = dict()
    # for d in get_digit(0, x[0] + x[1]): codes[0] += [c for c in d]
    for d in get_digit(1, x[0] + x[1]): codes[1] += [c for c in d]  #unique
    # for d in get_digit(2, x[0] + x[1]): codes[2] += [c for c in d]
    # for d in get_digit(3, x[0] + x[1]): codes[3] += [c for c in d]
    for d in get_digit(4, x[0] + x[1]): codes[4] += [c for c in d]  #unique
    # for d in get_digit(5, x[0] + x[1]): codes[5] += [c for c in d]
    # for d in get_digit(6, x[0] + x[1]): codes[6] += [c for c in d]
    for d in get_digit(7, x[0] + x[1]): codes[7] += [c for c in d]  #unique
    for d in get_digit(8, x[0] + x[1]): codes[8] += [c for c in d]  #unique
    # for d in get_digit(9, x[0] + x[1]): codes[9] += [c for c in d]
        
    # wiring["up"] = list(set(codes[7]) - set(codes[1]))
    # wiring["up left"] = list(set(codes[4]) - set(codes[1]))
    # wiring["up right"] = list(codes[1])
    # wiring["center"] = list(set(codes[4]) - set(codes[1]))
    # wiring["down left"] = list(set(codes[8]) - set(codes[4]) - set(wiring["up"]))
    # wiring["down right"] = list(codes[1])
    # wiring["down"] = list(set(codes[8]) - set(codes[4]) - set(wiring["up"]))
    # print(wiring)

    #digits[9] = [c for c in get_digit_by_len(6, x[0] + x[1]) if len(set(c).intersection(set(wiring["up left"]))) > 0 and len(set(c).intersection(set(wiring["center"]))) > 0 and len(set(c).intersection(set(wiring["up right"]))) > 0 and len(set(c).intersection(set(wiring["down right"]))) > 0]
    
    digits[1] = get_digit(1, x[0] + x[1])
    digits[4] = get_digit(4, x[0] + x[1])
    digits[7] = get_digit(7, x[0] + x[1])
    digits[8] = get_digit(8, x[0] + x[1])

    digits[3] = [c for c in get_digit_by_len(5, x[0] + x[1]) if len(set(c).intersection(codes[1])) == 2]
    digits[9] = [c for c in get_digit_by_len(6, x[0] + x[1]) if len(set(c).intersection(codes[4])) == 4]
    digits[0] = [c for c in get_digit_by_len(6, x[0] + x[1]) if c not in digits[9] and len(set(c).intersection(codes[7])) == 3]
    digits[6] = [c for c in get_digit_by_len(6, x[0] + x[1]) if c not in digits[9] and c not in digits[0]]
    digits[5] = [c for c in get_digit_by_len(5, x[0] + x[1]) if c not in digits[3] and len(set(c).intersection(set(codes[4]))) == 3]
    digits[2] = [c for c in get_digit_by_len(5, x[0] + x[1]) if c not in digits[3] and c not in digits[5]]

    decoder = dict()
    for k in digits.keys():
        for d in digits[k]:
            decoder[d] = k

    # print(x)
    # print(decoder)

    output = ""
    for d in x[1]:
        output += str(decoder[d])
    
    count += int(output)

    continue

    digs = get_digit_by_len(6, x[0] + x[1])
    for d in digs:
        s = set(d) - set(wiring['up']) - set(codes[4])
        if len(s) == 1:
            wiring["down"] = list(s)
            break
    
    digs = get_digit_by_len(5, x[0] + x[1])
    for d in digs:
        s = set(d) - set(wiring['down']) - set(codes[7])
        if len(s) == 1:
            wiring["center"] = list(s)
            break

    digs = get_digit_by_len(6, x[0] + x[1])
    for d in digs:
        s = set(d) - set(codes[7]) - set(wiring['center']) - set(wiring["down"])
        if len(s) == 1:
            wiring["up left"] = list(s)
            break
    
    digs = get_digit_by_len(5, x[0] + x[1])
    for d in digs:
        s = set(d) - set(wiring['up']) - set(wiring["up left"]) - set(wiring["center"]) - set(wiring["down"])
        if len(s) == 1:
            wiring["down right"] = list(s)
            break

    digs = get_digit_by_len(6, x[0] + x[1])
    for d in digs:
        s = set(d) - set(wiring['up']) - set(wiring["up left"]) - set(wiring["center"]) - set(wiring["down right"]) - set(wiring["down"])
        if len(s) == 1:
            wiring["up right"] = list(s)
            break
    
    digs = get_digit(8, x[0] + x[1])
    for d in digs:
        s = set(d) - set(wiring['up']) - set(wiring["up left"]) - set(wiring["up right"]) - set(wiring["center"]) - set(wiring["down"]) - set(wiring["down right"])
        if len(s) == 1:
            wiring["down left"] = list(s)
            break
    
    # fix_wiring(wiring)
    print("==========================================================")
    print(wiring)
    print("")
    output = ""
    for d in x[1]:
        print(d)
        output += str(digit2int(d, wiring))
    count += int(output)

print(f"Result: {count}")