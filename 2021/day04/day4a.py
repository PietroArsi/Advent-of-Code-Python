def check_matrix(x, y, matrix):
    row = [r for r in matrix[x] if r[1]==True]
    column = [r[y] for r in matrix if r[y][1]==True]
    if(len(column) == 5 or len(row) == 5):
        return True
    else:
        return False


with open("i4.txt", "r") as f:
    #data = [[y.strip() for y in x.split("\n\n")] for x in f.read()]
    data = [x.strip() for x in f.readlines() if x.strip()!=""]

numbers = [int(x) for x in data[0].split(",")]

mats=[]
for x in range(1, len(data[1:]), 5):
    mats.append([[(int(y), False) for y in x.split()] for x in data[x:x+5]])

winner_found=False
winner = -1
winner_number = -1
for num in range(len(numbers)):
    for x in range(len(mats)):
        for y in range(len(mats[x])):
            for z in range(len(mats[x][y])):
                if(mats[x][y][z][0] == numbers[num]):
                    mats[x][y][z] = (mats[x][y][z][0], True)
                    if(check_matrix(y,z,mats[x])):
                        winner = x
                        winner_number = numbers[num]
                        winner_found=True
                        break
                if(winner_found):
                    break
            if(winner_found):
                break
        if(winner_found):
            break
    if(winner_found):
        break

count = 0
for x in mats[winner]:
    for y in x:
        if(not y[1]):
            count+=y[0]

print(f"Result: {winner_number * count}")