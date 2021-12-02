import re

f=open("inputs/i12.txt","r")
lines=f.readlines()
f.close()
pattern="<x=\d*, y=\d*, z=\d*>"

moons=[]
velocity=[]
for x in range(len(lines)):
    lines[x]=re.sub(r"\n", "",lines[x])
    moons.append([0,0,0])
    velocity.append([0,0,0])
    z=re.findall(r"\d+|-\d+", lines[x])
    moons[x][0]=z[0]
    moons[x][1]=z[1]
    moons[x][2]=z[2]


steps=1000
analyzed_moons=[]
for x in range(steps):
    analyzed_moons.clear()
    #update velocity
    for moon1 in range(len(moons)):
        for moon2 in range(len(moons)):
            if(moon1!=moon2 and tuple([moon1, moon2]) not in analyzed_moons and tuple([moon2, moon1]) not in analyzed_moons):
                analyzed_moons.append(tuple([moon1, moon2]))
                #x variable
                if(int(moons[moon2][0])>int(moons[moon1][0])):
                    velocity[moon1][0]+=1
                    velocity[moon2][0]-=1
                elif(int(moons[moon2][0])<int(moons[moon1][0])):
                    velocity[moon1][0]-=1
                    velocity[moon2][0]+=1
                #y variable
                if(int(moons[moon2][1])>int(moons[moon1][1])):
                    velocity[moon1][1]+=1
                    velocity[moon2][1]-=1
                elif(int(moons[moon2][1])<int(moons[moon1][1])):
                    velocity[moon1][1]-=1
                    velocity[moon2][1]+=1
                #z variable
                if(int(moons[moon2][2])>int(moons[moon1][2])):
                    velocity[moon1][2]+=1
                    velocity[moon2][2]-=1
                elif(int(moons[moon2][2])<int(moons[moon1][2])):
                    velocity[moon1][2]-=1
                    velocity[moon2][2]+=1
    #update position
    for x in range(len(moons)):
        moons[x][0]=str(int(moons[x][0])+velocity[x][0])
        moons[x][1]=str(int(moons[x][1])+velocity[x][1])
        moons[x][2]=str(int(moons[x][2])+velocity[x][2])

# print(str(moons))

value=0
for x in range(len(moons)):
    value+=(abs(int(moons[x][0]))+abs(int(moons[x][1]))+abs(int(moons[x][2])))*(abs(velocity[x][0])+abs(velocity[x][1])+abs(velocity[x][2]))

print("Total energy after "+str(steps)+" steps is: "+str(value))