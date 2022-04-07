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
for x in range(len(data)):
    if data[x][5] is not None:
        current_id = data[x][5]
    else:
        data[x] = (data[x][0], data[x][1], data[x][2], data[x][3], data[x][4], int(current_id), data[x][6])

sleep_minutes = defaultdict(lambda: defaultdict(int))

for x in range(len(data)):
    if data[x][6] == "sleep":
        start = (int(data[x][3]), int(data[x][4]))
        eid = int(data[x][5])
    elif data[x][6] == "wake":
        finish = (int(data[x][3]), int(data[x][4]))

        curs = [start[0], start[1]]
        while(curs[0] != finish[0] or curs[1] != finish[1]):
            sleep_minutes[eid][(curs[0], curs[1])] += 1

            curs[1] += 1
            if curs[1] == 60:
                curs[1] = 0
                curs[0] += 1
            if curs[0] == 24:
                curs[0] = 0

sleep_leaderboard = list()
for i in sleep_minutes.keys():
    sleep_leaderboard.append((i, sum(sleep_minutes[i].values())))

sleep_leaderboard.sort(key=lambda x: x[1], reverse=True)
sleep_king = sleep_leaderboard[0][0]

best_minute = -1
best_minute_count = -1

for x in sleep_minutes[sleep_king].keys():
    if sleep_minutes[sleep_king][x] > best_minute_count:
        best_minute = (x[0], x[1])
        best_minute_count = sleep_minutes[sleep_king][x]

print(best_minute[1] * sleep_king)