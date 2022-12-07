import re
from collections import defaultdict
from functools import reduce

with open("2022/day07/input.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

# filesystem = dict()
# pointer = None

# filesystem["/"] = {
#     "type" : "dir",
#     "size" : 0
# }
# pointer = filesystem["/"]

# filesystem = list()
# filesystem.append(("/", None))

filesystem = dict()
dirs = dict()
filesystem["/"] = list()

pointer_stack = ["/"]
# print(filesystem)
# print(pointer_stack)

curs = 1
while curs < len(lines):
    a = re.match(r"^\$ cd ([^\.]+)$", lines[curs])
    b = re.match(r"^\$ ls$", lines[curs])
    c = re.match(r"^\$ cd \.\.$", lines[curs])
    d = re.match(r"^(\d+) (.+)$", lines[curs])
    e = re.match(r"^dir (.+)$", lines[curs])
    # print(filesystem)
    # print(pointer_stack)
    if a:
        # print(f"> move in {pointer_stack[-1] + a.group(1)}")
        if a.group(1) not in filesystem.keys():
            filesystem[pointer_stack[-1] + a.group(1)] = list()
        # dirs[a.group(1)] = pointer_stack[-1]
        pointer_stack.append(pointer_stack[-1] + a.group(1))
    elif b:
        pass
    elif c:
        pointer_stack.pop(len(pointer_stack)-1)
        # print(f"<<< move back to {pointer_stack[-1]}")
    elif d:
        # if pointer_stack[-1] not in filesystem.keys():
        #     filesystem[pointer_stack[-1]] = list()
        filesystem[pointer_stack[-1]].append((int(d.group(1)), d.group(2)))
    elif e:
        # if e.group(1) not in filesystem.keys():
        #     filesystem[e.group(1)] = list([0])
        dirs[pointer_stack[-1] + e.group(1)] = pointer_stack[-1]

    # if len(set(pointer_stack)) != len(pointer_stack):
    #     print(f"ERROREEEEEEEEEEEEEEEEEEE {curs}\n")
    #     print(dirs)
    #     print("")
    #     print(pointer_stack)
    #     break

    curs+=1

# for x in filesystem.keys():
#     print(x)
#     for y in filesystem[x]:
#         print(f"    {y}")

sizes = {}
for x in filesystem.keys():
    if len(filesystem[x]) > 0:
        sizes[x] = reduce(lambda a,b:a+b, [file[0] for file in filesystem[x]])
    else:
        sizes[x] = 0

# print(dirs)
to_evaluate = list()
for d in dirs.keys():
    to_evaluate.append((d, dirs[d]))

# print(to_evaluate)
while len(to_evaluate) > 0:
    temp = [x for x in to_evaluate]
    to_evaluate.clear()
    for link in temp:
        if link[0] not in [x[1] for x in temp]:
            # print(f"VALUTO {link}")
            sizes[link[1]] += sizes[link[0]]
            if link[1] != "/" and link[1] not in [x[0] for x in temp]:
                to_evaluate.append((link[1], dirs[link[1]]))
        else:
            # print(f"NON POSSO ANCORA VALUTARE {link}")
            to_evaluate.append((link[0], link[1]))
    # print(to_evaluate)

count = 0
for x in sizes:
    if sizes[x] <= 100000:
        count += sizes[x]

print(f"Result: {count}")