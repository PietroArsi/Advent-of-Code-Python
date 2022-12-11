import re
import math
from functools import reduce

class Monkey:
    def __init__(self):
        self.inspects = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
    
    def set_operation(self, op, arg2):
        self.op = op
        self.arg2 = arg2

    def set_check(self, div):
        self.div = div

    def set_throws(self, if_true, if_false):
        self.if_true = if_true
        self.if_false = if_false

    def __str__(self):
        return f"{self.items} {self.op} {self.arg2} {self.div} {self.if_true} {self.if_false}"

with open("2022/day11/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

monkeys = []
divs = []

for x in range(0, len(lines), 7):
    items = [int(a) for a in re.findall(r"(\d+)", lines[x+1])]
    operation = re.match(r"Operation: new = old (?:(\*)|(\+)) (?:(old)|(\d+))", lines[x+2])
    test = int(re.match(r"Test: divisible by (\d+)", lines[x+3]).group(1))
    test_true = int(re.match(r"If true: throw to monkey (\d+)", lines[x+4]).group(1))
    test_false = int(re.match(r"If false: throw to monkey (\d+)", lines[x+5]).group(1))

    divs.append(test)
    monkey = Monkey()

    for i in items: monkey.add(i)
    monkey.set_operation(operation.group(1) or operation.group(2), operation.group(3) or int(operation.group(4)))
    monkey.set_check(test)
    monkey.set_throws(test_true, test_false)

    monkeys.append(monkey)

factor = reduce(lambda a,b:a*b, divs)

turn = 0

while True:
    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            if monkey.op == "*":
                if monkey.arg2 == "old":
                    new_item = item * item
                else:
                    new_item = item * monkey.arg2
            elif monkey.op == "+":
                if monkey.arg2 == "old":
                    new_item = item + item
                else:
                    new_item = item + monkey.arg2
            
            monkey.inspects += 1
            if new_item % monkey.div == 0:
                monkeys[monkey.if_true].add(int(new_item % factor))
            else:
                monkeys[monkey.if_false].add(int(new_item % factor))

    turn += 1

    # print(f"Round {turn}")
    # for x in monkeys: print(f"{x.items} {x.inspects}")
    # print("")

    if turn == 10000:
        break

monkeys.sort(key=lambda a:a.inspects, reverse=True)
print(f"Activity: {monkeys[0].inspects * monkeys[1].inspects}")