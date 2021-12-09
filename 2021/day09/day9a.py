with open("i9.txt") as f: map = [[int(y) for y in x.strip()] for x in f.readlines()]

def is_low(a, b, mapt):
    x_dim = len(mapt[0])
    y_dim = len(mapt)
    if a == 0 or a > 0 and mapt[b][a] < mapt[b][a-1]:
        # if a == 0 or b == 0 or a > 0 and b > 0 and mapt[b][a] < mapt[b-1][a-1]:
        if b == 0 or b > 0 and mapt[b][a] < mapt[b-1][a]:
                # if b == 0 or a == x_dim-1 or b > 0 and a < x_dim-1 and mapt[b][a] < mapt[b-1][a+1]:
            if a == x_dim-1 or a < x_dim-1 and mapt[b][a] < mapt[b][a+1]:
                        # if a == x_dim-1 or b == y_dim-1 or a < x_dim-1 and b < y_dim-1 and mapt[b][a] < mapt[b+1][a+1]:
                if b == y_dim-1 or b < y_dim-1 and mapt[b][a] < mapt[b+1][a]:
                                # if b == y_dim-1 or a == 0 or b < y_dim-1 and a > 0 and mapt[b][a] < map[b+1][a-1]:
                    return True
    return False

lowpoints = []
for y in range(len(map)):
    for x in range(len(map[y])):
        if is_low(x, y, map):
            lowpoints.append((int(x),int(y)))

count = 0
for t in lowpoints:
    count += map[t[1]][t[0]] + 1

print(f"Risk level: {count}")