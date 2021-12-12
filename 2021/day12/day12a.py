from collections import defaultdict

class PathError(Exception):
    pass

class Path:
    path = []

    def __init__(self, first:str):
        self.path = []
        self.path.append(str(first))
    
    def set_path(self, to_copy:list):
        self.path = []
        for x in to_copy:
            self.add_step(str(x))
    
    def add_step(self, step):
        if not step.islower():
            self.path.append(str(step))
        elif step.islower() and step not in self.path:
            self.path.append(str(step))
        else:
            # print(f"ERROR: {step} already in path")
            raise PathError
    
    def get_path(self):
        return self.path

    def get_last(self):
        return str(self.path[-1])

    def has(self, step):
        return step in self.path

    def __str__(self):
        return ",".join(self.path)

with open("i12.txt") as f: lines = [x.strip() for x in f.readlines()]

map = defaultdict(set)
for x in lines:
    t = x.split("-")
    if t[0] == "end":
        map[t[1]].add(t[0])
    elif t[1] == "end":
        map[t[0]].add(t[1])
    elif t[0] == "start":
        map[t[0]].add(t[1])
    elif t[1] == "start":
        map[t[1]].add(t[0])
    else:
        map[t[0]].add(t[1])
        map[t[1]].add(t[0])

paths = []
for x in map["start"]:
    a = Path("start")
    a.add_step(x)
    paths.append(a)

# print(map)

proceeded = True
while proceeded:
    proceeded = False
    temp_paths = list(paths)
    new_paths = []

    for x in temp_paths:
        if x.get_last() in map and len(map[x.get_last()]) > 0:
            for next_step in map[x.get_last()]:
                try:
                    new = Path("start")
                    new.set_path(x.get_path())
                    new.add_step(next_step)
                    new_paths.append(new)
                    proceeded = True
                except PathError:
                    continue
        else:
            new_paths.append(x)
    paths = list(new_paths)
    new_paths.clear()

    # for x in paths:
    #     print(x)

print(f"Paths: {len(paths)}")