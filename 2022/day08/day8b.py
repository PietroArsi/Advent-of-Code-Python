with open("2022/day08/input.txt") as f:
    trees = [[int(y) for y in list(x.strip())] for x in f.readlines()]

MAX_X = len(trees)-1
MAX_Y = len(trees[0])-1

best_view = -1

for x in range(len(trees)):
    for y in range(len(trees[x])):
        if x == 0 or x == MAX_X or y == 0 or y == MAX_Y:
            pass
        else:
            left_view = 1
            path = reversed(trees[x][:y])
            for t in path:
                if t >= trees[x][y]:
                    break
                left_view += 1
            else:
                left_view -= 1

            right_view = 1
            path = trees[x][y+1:]
            for t in path:
                if t >= trees[x][y]:
                    break
                right_view += 1
            else:
                right_view -= 1

            up_view = 1
            path = reversed([tree[y] for tree in trees][:x])
            for t in path:
                if t >= trees[x][y]:
                    break
                up_view += 1
            else:
                up_view -= 1

            down_view = 1
            path = [tree[y] for tree in trees][x+1:]
            for t in path:
                if t >= trees[x][y]:
                    break
                down_view += 1
            else:
                down_view -= 1

            view = left_view * right_view * up_view * down_view
            if view > best_view:
                # print(f"{x} {y}: {left_view} {right_view} {up_view} {down_view}")
                best_view = int(view)

print(best_view)