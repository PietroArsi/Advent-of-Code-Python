import numpy
import re
import collections

f=open("inputs/i3.txt", "r")
lines=f.readlines()
f.close()

wire1=lines[0].split(",")
wire2=lines[1].split(",")

oldX1=0
oldY1=0
targetX1=0
targetY1=0

oldX2=0
oldY2=0
targetX2=0
targetY2=0

total_passi1=0
total_passi2=0

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

def manhattan_distance(x1, y1, x2, y2):
    return (abs(x2-x1) + abs(y2-y1))

for instr in wire1:
    passi1=int(re.sub("\D", "", instr))
    startX1=oldX1
    startY1=oldY1
    if(instr[0]=="R"):
        targetX1=startX1+passi1
        targetY1=startY1
    elif(instr[0]=="L"):
        targetX1=startX1-passi1
        targetY1=startY1
    elif(instr[0]=="U"):
        targetY1=startY1+passi1
        targetX1=startX1
    elif(instr[0]=="D"):
        targetY1=startY1-passi1
        targetX1=startX1

    #robe
    oldX2=0
    oldY2=0
    total_passi2=0
    for move in wire2:
        #print(str(instr)+" "+str(move))
        passi2=int(re.sub("\D", "", move))
        startX2=oldX2
        startY2=oldY2
        if(move[0]=="R"):
            #print("R2")
            targetX2=startX2+passi2
            targetY2=startY2
        elif(move[0]=="L"):
            #print("L2")
            targetX2=startX2-passi2
            targetY2=startY2
        elif(move[0]=="U"):
            #print("U2")
            targetY2=startY2+passi2
            targetX2=startX2
        elif(move[0]=="D"):
            #print("D2")
            targetY2=startY2-passi2
            targetX2=startX2
        
        # print("startX1: "+str(startX1)+", targetX1: "+str(targetX1)+", startX2: "+str(startX2)+", targetX2: "+str(targetX2))
        # print("startY1: "+str(startY1)+", targetY1: "+str(targetY1)+", startY2: "+str(startY2)+", targetY2: "+str(targetY2)+"\n")

        if(startY1==startY2==targetY1==targetY2):
            #stessa y
            x_values=intersection(list(range(startX1, targetX1+1)),list(range(startX2, targetX2+1)))
            if(x_values):
                #print("cross1")
                distance=total_passi1+total_passi2+manhattan_distance(startX1, startY1, startX2, startY2)
                if(("min_distance" not in locals() or distance<min_distance)and distance!=0):
                    min_distance=distance
        elif(startX1==startX2==targetX1==targetX2):
            #stessa x
            y_values=intersection(list(range(startY1, targetY1+1)),list(range(startY2, targetY2+1)))
            if(y_values):
                #print("cross2")
                distance=total_passi1+total_passi2+manhattan_distance(startX1, startY1, startX2, startY2)
                #distance=abs(startX1)+abs(min(y_values))
                if(("min_distance" not in locals() or distance<min_distance)and distance!=0):
                    min_distance=distance

        elif((instr[0]=="R")and(move[0]=="U" or move[0]=="D")and(startX2>=startX1 and startX2<=targetX1)and((startY2<=startY1 and startY2<=targetY1 and targetY2>=startY1 and targetY2>=targetY1)or(startY2>=startY1 and startY2>=targetY1 and targetY2<=startY1 and targetY2<=targetY1))):
            #find intersection point
            #print("cross3")
            #distance=abs(startX2)+abs(startY1)
            distance=total_passi1+manhattan_distance(startX1, startY1, startX2, startY1)+total_passi2+manhattan_distance(startX2, startY2, startX2, startY1)
            if(distance!=0 and ("min_distance" not in locals() or distance<min_distance)):
                min_distance=distance

        elif((instr[0]=="L")and(move[0]=="U" or move[0]=="D")and(startX2<=startX1 and startX2>=targetX1)and((startY2<=startY1 and startY2<=targetY1 and targetY2>=startY1 and targetY2>=targetY1)or(startY2>=startY1 and startY2>=targetY1 and targetY2<=startY1 and targetY2<=targetY1))):
            #find intersection point
            #print("cross4")
            #distance=abs(startX2)+abs(startY1)
            distance=total_passi1+manhattan_distance(startX1, startY1, startX2, startY1)+total_passi2+manhattan_distance(startX2, startY2, startX2, startY1)
            if(distance!=0 and ("min_distance" not in locals() or distance<min_distance)):
                min_distance=distance

        elif((instr[0]=="U")and(move[0]=="R" or move[0]=="L")and(startY2>=startY1 and startY2<=targetY1)and((startX2<=startX1 and startX2<=targetX1 and targetX2>=startX1 and targetX2>=targetX1)or(startX2>=startX1 and startX2>=targetX1 and targetX2<=startX1 and targetX2<=targetX1))):
            #print("cross5")
            #distance=abs(startX1)+abs(startY2)
            distance=total_passi1+manhattan_distance(startX1, startY1, startX1, startY2)+total_passi2+manhattan_distance(startX2, startY2, startX1, startY2)
            if(distance!=0 and ("min_distance" not in locals() or distance<min_distance)):
                min_distance=distance

        elif((instr[0]=="D")and(move[0]=="R" or move[0]=="L")and(startY2<=startY1 and startY2>=targetY1)and((startX2<=startX1 and startX2<=targetX1 and targetX2>=startX1 and targetX2>=targetX1)or(startX2>=startX1 and startX2>=targetX1 and targetX2<=startX1 and targetX2<=targetX1))):
            #print("cross6")
            #distance=abs(startX1)+abs(startY2)
            distance=total_passi1+manhattan_distance(startX1, startY1, startX1, startY2)+total_passi2+manhattan_distance(startX2, startY2, startX1, startY2)
            if(distance!=0 and ("min_distance" not in locals() or distance<min_distance)):
                min_distance=distance

        oldX2=targetX2
        oldY2=targetY2
        total_passi2+=passi2


    oldX1=targetX1
    oldY1=targetY1
    total_passi1+=passi1

#print(str(targetX1)+" "+str(targetY1))
if("min_distance" in locals()):
    print("Solution found: "+str(min_distance))
else:
    print("Solution not found...")

#(instr[0]=="U" or instr[0]=="D")and(move[0]=="R" or move[0]=="L")and