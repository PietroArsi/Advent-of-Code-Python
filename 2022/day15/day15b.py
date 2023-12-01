import re

with open("2022/day15/input.txt", encoding="utf-8") as f:
    lines = [x.strip() for x in f.readlines()]

# points = dict()
# for y in range(0, 4000000):
#     if y not in points.keys():
#         points[y] = set()
#     for x in range(0, 4000000):
#         points[y].add(x)

coords = []
sensors = set()
beacons = set()

for l in lines:
    m = re.match(r"^Sensor at x=(\d+), y=(\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$", l)
    coords.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), abs(int(m.group(1))-int(m.group(3))) + abs(int(m.group(2))-int(m.group(4)))))
    sensors.add((int(m.group(1)), int(m.group(2))))
    beacons.add((int(m.group(3)), int(m.group(4))))

signal_map = dict()

# esempio = (0, 11, 2, 10, 2)
# for y in range(esempio[1]-esempio[4], esempio[1]+esempio[4]+1):
#     dist = abs(esempio[1] - y)

#     if y not in signal_map.keys():
#         signal_map[y] = [esempio[0]-esempio[4] + dist, esempio[0]+esempio[4] - dist]
#     else:
#         if (esempio[0]-esempio[4] + dist) < signal_map[y][0]:
#             signal_map[y][0] = esempio[0]-esempio[4] + dist

#         if (esempio[0]+esempio[4] - dist) > signal_map[y][1]:
#             signal_map[y][1] = esempio[0]+esempio[4] - dist

for c in coords:
    for y in range(c[1]-c[4], c[1]+c[4]+1):
        dist = abs(c[1] - y)
        a = c[0]-c[4] + dist
        b = c[0]+c[4] - dist

        if y not in signal_map.keys():
            signal_map[y] = [(a, b)]
        else:
            done = False
            curs = 0
            while curs < len(signal_map[y]):
                i = signal_map[y][curs][0]
                j = signal_map[y][curs][1]
                if i <= a <= j or i <= b <= j:
                    done = True
                    signal_map[y].pop(curs)
                    signal_map[y].append((min(a,i), max(b,j)))
                    break
                curs += 1
            if not done:
                signal_map[y].insert(curs, (a,b))

        # for p in range(a, b+1):
        #     points[y].remove(p)

    # for y in range(9, 12):
    #     for x in range(-3, 15):
    #         if (x,y) in sensors:
    #             print("S", end="")
    #         elif (x,y) in beacons:
    #             print("B", end="")
    #         elif y in signal_map and len([1 for t in signal_map[y] if t[0] <= x <= t[1]])>0:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print("")
    # print("")

# y_signals = set(signal_map.keys())
# for y in range(0, limit):
#     found=False
#     for x in range(0, limit):
#         if y not in y_signals:
#             found=True
#             print(f"Result: {x*limit + y}")
#             break
#         else:
#             found2 = False
#             for t in signal_map[y]:
#                 if t[0] <= x <= t[1]:
#                     break
#             else:
#                 found2 = True
#             if found2:
#                 found=True
#                 print(f"Result: {x*4000000 + y}")
#                 break
#     if found:
#         break

# y_signals = set(signal_map.keys())
# y_list = [y for y in range(0, 4000000) if y not in y_signals]

print("checkpoint")

found = False
invalid = False
limit = 4000000

for y in range(0, 4000000):
    for x in range(0, 4000000):
        for r in signal_map[y]:
            if r[0] <= x <= r[1]:
                break
        else:
            break
    if found:
        break