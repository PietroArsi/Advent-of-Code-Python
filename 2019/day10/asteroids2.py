import math

f=open("inputs/i10.txt","r")
lines=f.readlines()
f.close()

def get_direction(pos1, pos2):
    #print("Finding GCD between "+str(pos1)+" and "+str(pos2))
    a=int((pos2[1]-pos1[1])/math.gcd(pos2[1]-pos1[1], pos2[0]-pos1[0]))
    b=int((pos2[0]-pos1[0])/math.gcd(pos2[1]-pos1[1], pos2[0]-pos1[0]))
    #print(str(b)+", "+str(a))
    return (b,a)

# count_dest=1
def shot_to(direction_to_shoot):
    base_direction_y=direction_to_shoot[0]
    base_direction_x=direction_to_shoot[1]
    direction_x=base_direction_x
    direction_y=base_direction_y
    # while((best_asteroid[1]+direction_x)!=ast[1] and (best_asteroid[0]+direction_y)!=ast[0]):
    while(True):
        #print("mltp: "+str(mltp))
        #robe
        if(map[best_asteroid[0]+direction_y][best_asteroid[1]+direction_x]=="#" and ((best_asteroid[0]+direction_y,best_asteroid[1]+direction_x) in remaining_asteroids)):
            #print("ahia "+str(offsetX)+", "+str(offsetY))
            asteroid=(best_asteroid[0]+direction_y,best_asteroid[1]+direction_x)
            break

        direction_x+=base_direction_x
        direction_y+=base_direction_y
    remaining_asteroids.remove(tuple(asteroid))
    destroyed_asteroids.append(tuple(asteroid))
    # global count_dest
    
    # if(count_dest==1 or count_dest==2 or count_dest==3 or count_dest==10 or count_dest==20 or count_dest==50 or count_dest==100 or count_dest==199 or count_dest==200 or count_dest==299):
    #     print("destroyed asteroid "+str(asteroid))
    # count_dest+=1
    

map=[]
count_map=[]
for x in range(len(lines)):
    map.append([])
    count_map.append([])
    for num in range(len(lines[x])):
        if(str(lines[x][num])!="\n"):
            count_map[x].append(0)
            map[x].append(str(lines[x][num]))

# for x in range(len(map)):
#     print(str(count_map[x]), end="\n")
X_limit=len(map[0])
Y_limit=len(map)


asteroids=list()
for y in range(len(map)):
    for x in range(len(map[y])):
        if(str(map[y][x])=="#"):
            asteroids.append((y, x))

max_asteroids=0
best_asteroid=[]
for ast1 in asteroids:
    count=0

    # if(ast1[0]>0):
    #     break
    for ast2 in asteroids:
        # print(str(ast1)+" and "+str(ast2))
        if(ast1[1]==ast2[1] and ast1[0]!=ast2[0]):
            #stessa X
            #print("xxx")
            y_values=[]
            y_values.clear()
            if(ast1[0]<=ast2[0]):
                for asd in range(ast1[0], ast2[0]):
                    y_values.append(int(asd))
            else:
                for asd in range(ast2[0], ast1[0]):
                    y_values.append(int(asd))
            if(y_values):
                del y_values[0]
            #print(str(y_values))

            check=False
            for Yval in y_values:
                if(map[Yval][ast1[1]]=="#"):
                    check=True
                    break
            if(check==False):
                #print("a")
                #f.write("a")
                count+=1
                
        elif(ast1[0]==ast2[0] and ast1[1]!=ast2[1]):
            #stessa Y
            #print("yyy")
            x_values=[]
            x_values.clear()
            if(ast1[1]<=ast2[1]):
                for asd in range(ast1[1], ast2[1]):
                    x_values.append(int(asd))
            else:
                for asd in range(ast2[1], ast1[1]):
                    x_values.append(int(asd))
            if(x_values):
                del x_values[0]
            #print(str(x_values))

            check=False
            for Xval in x_values:
                if(map[ast1[0]][Xval]=="#"):
                    check=True
                    break
            if(check==False):
                #print("a")
                #f.write("a")
                count+=1

        
        elif(ast1[0]!=ast2[0] and ast1[1]!=ast2[1]):
            base_offsetX=int((ast2[1]-ast1[1])/math.gcd(ast2[1]-ast1[1], ast2[0]-ast1[0]))
            base_offsetY=int((ast2[0]-ast1[0])/math.gcd(ast2[1]-ast1[1], ast2[0]-ast1[0]))
            #print(str(offsetX)+", "+str(offsetY))
            check=False
            offsetX=base_offsetX
            offsetY=base_offsetY
            while((ast1[1]+offsetX)!=ast2[1] and (ast1[0]+offsetY)!=ast2[0]):
                #print("mltp: "+str(mltp))
                #robe
                if(map[ast1[0]+offsetY][ast1[1]+offsetX]=="#"):
                    #print("ahia "+str(offsetX)+", "+str(offsetY))
                    check=True
                    break

                offsetX+=base_offsetX
                offsetY+=base_offsetY
            if(check==False):
                #print("a")
                #f.write("a")
                count+=1
        #f.write("\n")
         
    count_map[ast1[0]][ast1[1]]=int(count)
    if(count>max_asteroids):
        max_asteroids=int(count)
        best_asteroid=tuple(ast1)

# for x in count_map:
#     print(str(x))
#f.close()
print("Best asteroid is: ("+str(best_asteroid[1])+", "+str(best_asteroid[0])+")"+" with "+str(max_asteroids)+" asteroids.")

cannon_angle=-(math.pi/2)-0.000001
destroyed_asteroids=list()
remaining_asteroids=list(asteroids)
print("Cannon mounted...")
#print(str(cannon_angle))

# print(str(remaining_asteroids[0]))
# print(str(remaining_asteroids))
# for x in remaining_asteroids:
#     print(str(x))

final_result=list()
final_result.append(best_asteroid)
count_dest=1
while(remaining_asteroids!=final_result):
    check=False
    for ast in remaining_asteroids:
        if(ast!=best_asteroid):
            dir=get_direction(best_asteroid, ast)
            angle=math.atan2(dir[0], dir[1])
            if(angle<cannon_angle):
                angle=math.pi + abs(angle)
            if(check==False):
                if(angle>cannon_angle):
                    #print("Updated")
                    check=True
                    next_angle=angle
                    next_direction=dir
                    to_destroy=ast
            elif(cannon_angle<angle<next_angle):
                #print("Updated")
                next_angle=angle
                next_direction=dir
                to_destroy=ast
    #shot in right direction
    #print("Shot direction: "+str(next_direction))
    shot_to(next_direction)
    cannon_angle=next_angle
    if(cannon_angle>=math.pi):
        rest=cannon_angle-math.pi
        cannon_angle=-math.pi+rest
    # print(str(cannon_angle))
    # print(str(remaining_asteroids))

if(200<=len(destroyed_asteroids)):
    print("200th destroyed asteroid is: ("+str(destroyed_asteroids[199][1])+", "+str(destroyed_asteroids[199][0])+"), so the solution is: "+str(int(destroyed_asteroids[199][1])*100+int(destroyed_asteroids[199][0])))
else:
    print("Error, destroyed only "+str(len(destroyed_asteroids))+" asteroids")