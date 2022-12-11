import re

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

def factorization(num):
    value = int(num)
    result = dict()
    i = 2
    while i <= num:
        if value % i == 0:
            value = value/i
            if i not in result.keys():
                result[i]=0
            result[i] += 1
        else:
            i += 1
    return result

def defactorization(num):
    result = 1
    for x in num.keys():
        result = result * (x**num[x])
    return result

def is_div(num1, num2):
    for x in num2.keys():
        if x not in num1.keys() or num2[x] > num1[x]:
            return False
    return True 

with open("2022/day11/test.txt") as f:
    lines = [x.strip() for x in f.readlines()]

monkeys = []
for x in range(0, len(lines), 7):
    items = [int(a) for a in re.findall(r"(\d+)", lines[x+1])]
    operation = re.match(r"Operation: new = old (?:(\*)|(\+)) (?:(old)|(\d+))", lines[x+2])
    test = int(re.match(r"Test: divisible by (\d+)", lines[x+3]).group(1))
    test_true = int(re.match(r"If true: throw to monkey (\d+)", lines[x+4]).group(1))
    test_false = int(re.match(r"If false: throw to monkey (\d+)", lines[x+5]).group(1))

    monkey = Monkey()

    for i in items: monkey.add(factorization(i))
    monkey.set_operation(operation.group(1) or operation.group(2), operation.group(3) or int(operation.group(4)))
    monkey.set_check(factorization(test))
    monkey.set_throws(test_true, test_false)

    monkeys.append(monkey)

turn = 0

while True:
    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)

            if monkey.op == "*":
                if monkey.arg2 == "old":
                    second = item
                    # new_item = {k: item.get(k, 0) + second.get(k, 0) for k in set(item) | set(second)}
                else:
                    second = factorization(monkey.arg2)
                    # new_item = {k: item.get(k, 0) + second.get(k, 0) for k in set(item) | set(second)}
            elif monkey.op == "+":
                if monkey.arg2 == "old":
                    new_item = item
                    if 2 in new_item.keys():
                        new_item[2] += 1
                    else:
                        new_item[2] = 1
                    # second = factorization(defactorization(item) * 2)
                    # new_item = {k: item.get(k, 0) + second.get(k, 0) for k in set(item) | set(second)}
                else:
                    second = factorization(defactorization(item) + monkey.arg2)
            new_item = {k: item.get(k, 0) + second.get(k, 0) for k in set(item) | set(second)}

            monkey.inspects += 1
            
            if is_div(new_item, monkey.div):
                monkeys[monkey.if_true].add(new_item)
            else:
                monkeys[monkey.if_false].add(new_item)

    turn += 1

    print(f"Round {turn}")
    # for x in monkeys: print(f"{x.inspects}")

    if turn == 10000:
        break

monkeys.sort(key=lambda a:a.inspects, reverse=True)
print(monkeys[0].inspects * monkeys[1].inspects)