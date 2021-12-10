with open("i10.txt") as f: data = [list(x.strip()) for x in f.readlines()]

points = dict()
points[")"] = {"value": 1, "opener": "("}
points["]"] = {"value": 2, "opener": "["}
points["}"] = {"value": 3, "opener": "{"}
points[">"] = {"value": 4, "opener": "<"}

openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]

scores = []
for line in data:
    queue = []
    extra_closers = []
    wrong = False

    for c in line:
        if c in openers:
            queue.append(c)
        elif c in closers:
            if len(queue) > 0:
                last = queue.pop(-1)
                if points[c]["opener"] != last:
                    wrong = True
                    break

    for c in reversed(queue):
        extra_closers.append(next(key for key, value in points.items() if value["opener"] == c))
    
    # print(f"{''.join(queue)} {''.join(extra_closers)}")

    if not wrong:
        count = 0
        for c in extra_closers:
            count *= 5
            count += points[c]["value"]
        scores.append(int(count))

scores.sort()

print(f"Middle score: {scores[len(scores)//2]}")