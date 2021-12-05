def add_tup(t, ps, eps):
    global count
    # if(t in ps and t in eps):
    #     eps.append(t)
    # elif(t in ps and t not in eps):
    #     count += 1
    #     eps.append(t)
    # elif (not t in ps and not t in eps):
    #     points.add(t)
    if(t[0] in ps.keys()):
        if(t[1] in ps[t[0]]):
            if (t[0] in eps.keys() and t[1] in eps[t[0]]):
                eps[t[0]].append(t[1])
            elif(t[0] in eps.keys() and t[1] not in eps[t[0]]):
                count += 1
                eps[t[0]].append(t[1])
            elif(t[0] not in eps.keys()):
                count += 1
                eps[t[0]] = list()
                eps[t[0]].append(t[1])
        else:
            ps[t[0]].append(t[1])
    else:
        ps[t[0]] = list()
        ps[t[0]].append(t[1])

with open('i5.txt', 'r') as f:
    data = [[[int(z) for z in y.split(",")] for y in x.strip().split(" -> ")] for x in f.readlines()]

points = dict()
extra_points = dict()
count = 0
for x in data:
    if (x[0][0] == x[1][0]):
        # x1 = x2
        coord = x[0][0]
        min_y = min(x[0][1], x[1][1])
        max_y = max(x[0][1], x[1][1])

        for p in range(min_y, max_y + 1):
            tup = (int(coord), int(p))
            add_tup(tup, points, extra_points)
    elif (x[0][1] == x[1][1]):
        # y1 = y2
        coord = x[0][1]
        min_x = min(x[0][0], x[1][0])
        max_x = max(x[0][0], x[1][0])
        for p in range(min_x, max_x + 1):
            tup = (int(p), int(coord))
            add_tup(tup, points, extra_points)
    else:
        # print(x)
        x_diff = x[1][0] - x[0][0]
        if(x[1][0] > x[0][0] and x[1][1] > x[0][1]):
            # x1 > x2 and y1 > y2
            quadrante = 1
        elif(x[1][0] < x[0][0] and x[1][1] > x[0][1]):
            # x1 < x2 and y1 > y2
            quadrante = 2
        elif(x[1][0] < x[0][0] and x[1][1] < x[0][1]):
            # x1 < x2 and y1 < y2
            quadrante = 3
        elif(x[1][0] > x[0][0] and x[1][1] < x[0][1]):
            # x1 > x2 and y1 < y2
            quadrante = 4

        # print(f"Quadrante: {quadrante}")
        if(quadrante == 1):
            for diff in range(abs(x[1][0] - x[0][0]) + 1):
                i = x[0][0] + diff
                j = x[0][1] + diff
                tup = (int(i), int(j))
                # print(f"-> {tup}")
                add_tup(tup, points, extra_points)
        elif(quadrante == 2):
            for diff in range(abs(x[1][0] - x[0][0]) + 1):
                i = x[0][0] - diff
                j = x[0][1] + diff
                tup = (int(i), int(j))
                # print(f"-> {tup}")
                add_tup(tup, points, extra_points)
        elif(quadrante == 3):
            for diff in range(abs(x[1][0] - x[0][0]) + 1):
                i = x[0][0] - diff
                j = x[0][1] - diff
                tup = (int(i), int(j))
                # print(f"-> {tup}")
                add_tup(tup, points, extra_points)
        elif(quadrante == 4):
            for diff in range(abs(x[1][0] - x[0][0]) + 1):
                i = x[0][0] + diff
                j = x[0][1] - diff
                tup = (int(i), int(j))
                # print(f"-> {tup}")
                add_tup(tup, points, extra_points)

print(f"Result: {count}")

# map = [[0 for x in range(10)] for y in range(10)]

# for x in points:
#     map[x[1]][x[0]] += 1
# for x in extra_points:
#     map[x[1]][x[0]] += 1

# for x in map:
#     print(" ".join([str(y) for y in x]))