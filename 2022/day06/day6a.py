with open("2022/day06/input.txt") as f:
    signal = list(f.readlines()[0].strip())

curs = 3
while True:
    # print(signal[curs-3:curs+1])
    if len(set(signal[curs-3:curs+1])) == 4:
        break
    curs+=1

print(curs+1)

curs = 13
while True:
    # print(signal[curs-3:curs+1])
    if len(set(signal[curs-13:curs+1])) == 14:
        break
    curs+=1

print(curs+1)