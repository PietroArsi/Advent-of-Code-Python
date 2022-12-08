with open("2022/day08/input.txt") as f:
    trees = [[int(y) for y in list(x.strip())] for x in f.readlines()]

MIN_X = 0
MIN_Y = 0
MAX_X = len(trees)-1
MAX_Y = len(trees[0])-1

count = 0

for x in range(len(trees)):
    for y in range(len(trees[x])):
        if x == 0 or x == MAX_X or y == 0 or y == MAX_Y:
            # print("O", end="")
            count += 1
        else:
            if trees[x][y] > max(trees[x][:y]) or trees[x][y] > max(trees[x][y+1:]):
                # print(trees[x][:y+1], end="")
                # print("A", end="")
                count += 1
            elif trees[x][y] > max([tree[y] for tree in trees][:x]) or trees[x][y] > max([tree[y] for tree in trees][x+1:]):
                # print([tree[y] for tree in trees][:x], end="")
                # print("B", end="")
                count += 1

print(count)