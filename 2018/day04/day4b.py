import re
from collections import defaultdict

with open("i4.txt") as f:
    lines = [x.strip() for x in f.readlines()]

regex1 = r"^\[(\d+)-(\d+)-(\d+)\s(\d+):(\d+)\]\sGuard\s#(\d+)\sbegins\sshift$"
regex2 = r"^\[(\d+)-(\d+)-(\d+)\s(\d+):(\d+)\]\swakes\sup$"
regex3 = r"^\[(\d+)-(\d+)-(\d+)\s(\d+):(\d+)\]\sfalls\sasleep$"

data = []   # list of tuples (year, month, day, hour, minute, guard_id, action)
for line in lines:
    x1 = re.match(regex1, line)
    x2 = re.match(regex2, line)
    x3 = re.match(regex3, line)
    if x1:
        data.append((int(x1.group(1)), int(x1.group(2)), int(x1.group(3)), int(x1.group(4)), int(x1.group(5)), int(x1.group(6)), "begin"))
    elif x2:
        data.append((int(x2.group(1)), int(x2.group(2)), int(x2.group(3)), int(x2.group(4)), int(x2.group(5)), None, "wake"))
    elif x3:
        data.append((int(x3.group(1)), int(x3.group(2)), int(x3.group(3)), int(x3.group(4)), int(x3.group(5)), None, "sleep"))

data.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4]))

current_id = -1
id_set = set()
for x in range(len(data)):
    if data[x][5] is not None:
        current_id = data[x][5]
        id_set.add(int(current_id))
    else:
        data[x] = (data[x][0], data[x][1], data[x][2], data[x][3], data[x][4], int(current_id), data[x][6])

sleep_minutes = defaultdict(lambda: defaultdict(int))
minute_set = set()
for x in range(len(data)):
    if data[x][6] == "sleep":
        start = (int(data[x][3]), int(data[x][4]))
        eid = int(data[x][5])
    elif data[x][6] == "wake":
        finish = (int(data[x][3]), int(data[x][4]))

        curs = [start[0], start[1]]
        while(curs[0] != finish[0] or curs[1] != finish[1]):
            sleep_minutes[eid][(curs[0], curs[1])] += 1
            minute_set.add((int(curs[0]), int(curs[1])))
            curs[1] += 1
            if curs[1] == 60:
                curs[1] = 0
                curs[0] += 1
            if curs[0] == 24:
                curs[0] = 0

sleep_spot = (-1, -1)
sleep_record = -1
sleep_champion = -1
for t in minute_set:
    for i in id_set:
        if sleep_minutes[i][t] > sleep_record:
            sleep_record = int(sleep_minutes[i][t])
            sleep_champion = int(i)
            sleep_spot = (t[0], t[1])

print(sleep_champion * sleep_spot[1])