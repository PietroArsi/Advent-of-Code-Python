with open("i10.txt") as f: data = [list(x.strip()) for x in f.readlines()]

points = dict()
points[")"] = {"value": 3, "opener": "("}
points["]"] = {"value": 57, "opener": "["}
points["}"] = {"value": 1197, "opener": "{"}
points[">"] = {"value": 25137, "opener": "<"}

openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]

queue = []
syntax_error_score = 0
for line in data:
    for c in line:
        if c in openers:
            queue.append(c)
        elif c in closers:
            if len(queue) > 0:
                last = queue.pop(-1)
                if points[c]["opener"] != last:
                    syntax_error_score += points[c]["value"]

print(f"Syntax error score: {syntax_error_score}")