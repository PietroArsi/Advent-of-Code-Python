with open("2022/day02/input.txt") as f:
    lines = [(x.strip()[0], x.strip()[2]) for x in f.readlines()]

victory_list = [("A", "Y"), ("B", "Z"), ("C", "X")]

score = 0
for l in lines:
    score += (l[1]=="X" and 1) or (l[1]=="Y" and 2) or (l[1]=="Z" and 3)
    score += (l in victory_list and 6) or ((l[0]=="A" and l[1]=="X" or l[0]=="B" and l[1]=="Y" or l[0]=="C" and l[1]=="Z") and 3) or 0

print(score)

score = 0
for l in lines:
    score += (l[1]=="X" and 0) or (l[1]=="Y" and 3) or (l[1]=="Z" and 6)
    score += (((l[0]=="A" and 0) or (l[0]=="B" and 1) or (l[0]=="C" and 2)) + ((l[1]=="X" and -1) or (l[1]=="Y" and 0) or (l[1]=="Z" and 1)))%3 + 1

print(score)
