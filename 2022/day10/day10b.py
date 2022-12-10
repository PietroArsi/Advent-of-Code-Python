from functools import reduce

class ActionQueue:
    def __init__(self):
        self.queue = []
        # self.X = 1
    def enqueue(self, action:tuple):
        self.queue.append(action)
    def action(self, x:int):
        if len(self.queue) > 0:
            action = self.queue.pop(0)
            if action[0] == "noop" or action[0]=="wait":
                return x
            elif action[0] == "addx":
                #self.X += action[1]
                return x + action[1]
        else:
            raise Exception("No actions left")
    def __str__(self):
        return ", ".join([f"{x[0]} {x[1]}" for x in self.queue])

with open("2022/day10/input.txt") as f:
    instructions = [x.strip() for x in f.readlines()]

queue = ActionQueue()

for i in instructions:
    if i == "noop":
        queue.enqueue(("noop", 0))
    if i.split(" ")[0] == "addx":
        queue.enqueue(("wait", 0))
        queue.enqueue(("addx", int(i.split(" ")[1])))

x = 1
step = 0
pixels = []

while True:
    print(f"x: {x}, step: {step} -> ", end="")
    if step%40 in [x-1, x, x+1]:
        print("True")
        pixels.append(True)
    else:
        print("False")
        pixels.append(False)

    try:
        x = queue.action(x)
    except Exception as e:
        break
    step += 1
    # print(x)

print(pixels)

for x in range(len(pixels)):
    if pixels[x] == True:
        print("#", end="")
    else:
        print(".", end="")
    if (x+1) % 40 == 0:
        print("")