import re

with open("2022/day15/input.txt", encoding="utf-8") as f:
    lines = [x.strip() for x in f.readlines()]

coords = []
sensors = set()
beacons = set()

for l in lines:
    m = re.match(r"^Sensor at x=(\d+), y=(\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$", l)
    coords.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), abs(int(m.group(1))-int(m.group(3))) + abs(int(m.group(2))-int(m.group(4)))))
    sensors.add((int(m.group(1)), int(m.group(2))))
    beacons.add((int(m.group(3)), int(m.group(4))))

#      --
#      21012
#.................
#........#........ -2
#.......###....... -1
#......##S#B......  0
#.......###.......  1
#........#........  2
#.................

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

        if y not in signal_map.keys():
            signal_map[y] = [c[0]-c[4] + dist, c[0]+c[4] - dist]
        else:
            if (c[0]-c[4] + dist) < signal_map[y][0]:
                signal_map[y][0] = c[0]-c[4] + dist

            if (c[0]+c[4] - dist) > signal_map[y][1]:
                signal_map[y][1] = c[0]+c[4] - dist

# for y in range(-1, 27):
#     for x in range(-3, 26):
#         if (x,y) in sensors:
#             print("S", end="")
#         elif (x,y) in beacons:
#             print("B", end="")
#         elif y in signal_map and (signal_map[y][0] <= x <= signal_map[y][1]):
#             print("#", end="")
#         else:
#             print(".", end="")
#     print("")

target = 2000000
missings = [1 for s in beacons.union(sensors) if s[1] == target and (s[1] not in signal_map.keys() or not (signal_map[s[1]][0] <= s[0] <= signal_map[s[1]][1]))]
print(signal_map[target][1] - signal_map[target][0] + len(missings))
