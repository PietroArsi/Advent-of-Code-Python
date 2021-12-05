from collections import defaultdict

with open('i5.txt', 'r') as f:
    data = [[[int(z) for z in y.split(",")] for y in x.strip().split(" -> ")] for x in f.readlines()]

points = defaultdict(int)
for x in data:
    if (x[0][0] == x[1][0]):
        # x1 = x2
        coord = x[0][0]
        min_y = min(x[0][1], x[1][1])
        max_y = max(x[0][1], x[1][1])
        for p in range(min_y, max_y + 1):
            tup = (int(coord), int(p))
            points[tup] += 1
    elif (x[0][1] == x[1][1]):
        # y1 = y2
        coord = x[0][1]
        min_x = min(x[0][0], x[1][0])
        max_x = max(x[0][0], x[1][0])
        for p in range(min_x, max_x + 1):
            tup = (int(p), int(coord))
            points[tup] += 1
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
                points[tup] += 1
        elif(quadrante == 2):
            for diff in range(abs(x[1][0] - x[0][0]) + 1):
                i = x[0][0] - diff
                j = x[0][1] + diff
                tup = (int(i), int(j))
                # print(f"-> {tup}")
                points[tup] += 1
        elif(quadrante == 3):
            for diff in range(abs(x[1][0] - x[0][0]) + 1):
                i = x[0][0] - diff
                j = x[0][1] - diff
                tup = (int(i), int(j))
                # print(f"-> {tup}")
                points[tup] += 1
        elif(quadrante == 4):
            for diff in range(abs(x[1][0] - x[0][0]) + 1):
                i = x[0][0] + diff
                j = x[0][1] - diff
                tup = (int(i), int(j))
                # print(f"-> {tup}")
                points[tup] += 1

count = 0
for x in points.keys():
    if(points[x] > 1):
        count += 1

print(f"Result: {count}")