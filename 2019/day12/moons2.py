import re
import time
import math

start_time = time.time()

f=open("inputs/i12.txt","r")
lines=f.readlines()
f.close()
pattern="<x=\d*, y=\d*, z=\d*>"

moons=[]
moons_originals=[]
periods=[[-1,-1,-1]]
periods_v=[[-1,-1,-1]]
velocity=[]
for x in range(len(lines)):
    lines[x]=re.sub(r"\n", "",lines[x])
    moons.append([0,0,0])
    moons_originals.append([0,0,0])
    velocity.append([0,0,0])
    z=re.findall(r"\d+|-\d+", lines[x])
    moons[x][0]=int(z[0])
    moons[x][1]=int(z[1])
    moons[x][2]=int(z[2])
    moons_originals[x][0]=int(z[0])
    moons_originals[x][1]=int(z[1])
    moons_originals[x][2]=int(z[2])
#print(str(moons_originals))

#print(str(moons))
# print(str(moons_originals))

universe_state=set()

#steps=1000
steps=0
analyzed_moons=[]
#for x in range(steps):
while(True):
    analyzed_moons.clear()
    #update velocity
    for moon1 in range(len(moons)):
        for moon2 in range(len(moons)):
            # if(moons[1]==["5", "5", "-9"] and velocity[1]==[0,0,0]):
            #     print("aaa "+str(steps))
            if(moon1!=moon2 and tuple([moon1, moon2]) not in analyzed_moons and tuple([moon2, moon1]) not in analyzed_moons):
                analyzed_moons.append(tuple([moon1, moon2]))
                #x variable
                if((moons[moon2][0])>(moons[moon1][0])):
                    velocity[moon1][0]+=1
                    velocity[moon2][0]-=1
                elif((moons[moon2][0])<(moons[moon1][0])):
                    velocity[moon1][0]-=1
                    velocity[moon2][0]+=1
                #y variable
                if((moons[moon2][1])>(moons[moon1][1])):
                    velocity[moon1][1]+=1
                    velocity[moon2][1]-=1
                elif((moons[moon2][1])<(moons[moon1][1])):
                    velocity[moon1][1]-=1
                    velocity[moon2][1]+=1
                #z variable
                if((moons[moon2][2])>(moons[moon1][2])):
                    velocity[moon1][2]+=1
                    velocity[moon2][2]-=1
                elif((moons[moon2][2])<(moons[moon1][2])):
                    velocity[moon1][2]-=1
                    velocity[moon2][2]+=1
    # if(steps==10):
    #     print(str(moons[0][0]))
    #     print(str(moons_originals[0][0]))
    #update position
    for x in range(len(moons)):
        moons[x][0]=moons[x][0]+velocity[x][0]
        moons[x][1]=moons[x][1]+velocity[x][1]
        moons[x][2]=moons[x][2]+velocity[x][2]
    steps+=1
    #print(str(steps))
    # if(tuple([moons, velocity]) in universe_state):
    #     break
    # else:
    #     universe_state.add(tuple([moons, velocity]))
    # print(str(moons))
    # print(str(moons_originals))
    # zeroed=0
    # if(steps==2772):
    #     print(str(steps))
    #     print(str(moons))
    #     print(str(velocity))

    # for var in range(len(moons)):
    #     if(period[var][1]==False and moons[var][0]==moons_originals[var][0] and moons[var][1]==moons_originals[var][1] and moons[var][2]==moons_originals[var][2] and velocity[var]==[0,0,0]):
    #         period[var][1]=True
    #         period[var][0]=steps
    #         print(str(var))
    #         print(str(moons[var])+" "+str(velocity[var])+" after "+str(steps)+" steps")

    # if(steps==1000):
    #     value=0
    #     for x in range(len(moons)):
    #         value+=(abs(int(moons[x][0]))+abs(int(moons[x][1]))+abs(int(moons[x][2])))*(abs(velocity[x][0])+abs(velocity[x][1])+abs(velocity[x][2]))
    #     print("After 1000 steps, total energy is "+str(value))

    # if(steps==2772):
    #     print(str(moons[0]))
    #     print(str(moons_originals[0]))

    for rip in range(3):
        if(moons[0][rip]==moons_originals[0][rip] and moons[1][rip]==moons_originals[1][rip] and moons[2][rip]==moons_originals[2][rip] and moons[3][rip]==moons_originals[3][rip] and velocity[0][rip]==0 and velocity[1][rip]==0 and velocity[2][rip]==0 and velocity[3][rip]==0 and periods[0][rip]==-1):
            periods[0][rip]=int(steps)

    # for rip2 in range(3):
    #     if(velocity[0][rip2]==0 and velocity[1][rip2]==0 and velocity[2][rip2]==0 and velocity[3][rip2]==0 and periods_v[0][rip2]==-1):
    #         periods_v[0][rip2]=int(steps)

    # print(str(periods))
    # print(str(periods_v))
    period_found=True

    #print(str(periods))
    #print(str(periods_v))

    for y in range(3):
        if(periods[0][y]==-1):
            period_found=False
            break

    if(period_found==True):
        periods_t=[]
        for ccc in range(3):
            periods_t.append(int(periods[0][ccc]))
            #periods_t.append(int(periods_v[0][ccc]))

        lcm = periods_t[0]
        for i in periods_t[1:]:
            lcm = int(lcm*i/math.gcd(lcm, i))
        
        result=str(lcm)
        break

print("--- %s seconds ---" % (time.time() - start_time))
#print(str(steps))
print("Universe returns to his state in "+result+" steps")