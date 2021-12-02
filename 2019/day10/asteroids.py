import math

f=open("inputs/i10.txt","r")
lines=f.readlines()
f.close()

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
        best_asteroid=list(ast1)

# for x in count_map:
#     print(str(x))
#f.close()
print("Best asteroid is: ("+str(best_asteroid[1])+", "+str(best_asteroid[0])+")"+" with "+str(max_asteroids)+" asteroids.")

