with open('i5.txt', 'r') as f:
    data = [[[int(z) for z in y.split(",")] for y in x.strip().split(" -> ")] for x in f.readlines()]

# print(data)

points = set()
extra_points = list()
count = 0
for x in data:
    # print(f"A: {x[0]}, B: {x[1]}")
    if (x[0][0] == x[1][0]):
        # x1 = x2
        coord = x[0][0]
        # print("x1 == x2")
        min_y = min(x[0][1], x[1][1])
        max_y = max(x[0][1], x[1][1])

        for p in range(min_y, max_y + 1):
            tup = (int(coord), int(p))
            # print(f"-> {tup}")
            if(tup in points and tup in extra_points):
                extra_points.append(tup)
            elif(tup in points and tup not in extra_points):
                extra_points.append(tup)
                count += 1
            elif (tup not in points and tup not in extra_points):
                points.add(tup)
    elif (x[0][1] == x[1][1]):
        # y1 = y2
        coord = x[0][1]
        # print("y1 == y2")
        min_x = min(x[0][0], x[1][0])
        max_x = max(x[0][0], x[1][0])
        for p in range(min_x, max_x + 1):
            tup = (int(p), int(coord))
            # print(f"-> {tup}")
            if(tup in points and tup in extra_points):
                extra_points.append(tup)
            elif(tup in points and tup not in extra_points):
                count += 1
                extra_points.append(tup)
            elif (not tup in points and not tup in extra_points):
                points.add(tup)
    # print("")

print(f"Result: {count}")

# map = [[0 for x in range(10)] for y in range(10)]

# for x in points:
#     map[x[1]][x[0]] += 1
# for x in extra_points:
#     map[x[1]][x[0]] += 1

# for x in map:
#     print(" ".join([str(y) for y in x]))