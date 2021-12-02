import re

# class object:
#     def __init__(self, name):
#         self.name=name
#         self.sons=[]
#         self.father=None

f=open("i6.txt", "r")
lines=f.readlines()
f.close

orbits=[]
for line in lines:
    ob=line.split(")")
    orbits.append([ob[0], re.sub("\n", "", ob[1])])

# print(orbits[0][0]+" "+orbits[0][1])
# print(orbits[1][0]+" "+orbits[1][1])

#map={}
ob_orbits=set([])
ob_names=[]

for x in range(0, len(orbits)):
    if orbits[x][0] not in ob_names:
        ob_names.append(orbits[x][0])
    if orbits[x][1] not in ob_names:
        ob_names.append(orbits[x][1])
    
    ob_orbits.add((orbits[x][1],orbits[x][0]))
        
count=0
print("Set dimension: "+str(len(ob_orbits)))

#la parte brutta
# for x in range(len(ob_names)):
#     look_for=ob_names[x]
#     while(True):
#         # if(x==0):
#         #     print("Looking for "+look_for)
#         pool=[i for i in ob_orbits if i[0] == look_for]
#         if pool:
#             #print("Look up dimension is "+str(len(pool)))
#             count+=1
#             look_for=pool[0][1]
#         else:
#             break
pool=[i for i in ob_orbits if i[0] == "YOU"]
YOU_orbit=pool[0][1]
pool=[i for i in ob_orbits if i[0] == "SAN"]
SAN_orbit=pool[0][1]

#YOU path
YOU_path=set()
look_for=YOU_orbit
YOU_path.add(look_for)
while(True):
    pool=[i for i in ob_orbits if i[0] == look_for]
    if pool:
        look_for=pool[0][1]
        YOU_path.add(look_for)
    else:
        break

#SAN path
#SAN_path=set()
look_for=SAN_orbit
#SAN_path.add(look_for)
while(True):
    pool=list([i for i in ob_orbits if i[0] == look_for])
    if pool:
        # print("pool[0][0] is "+str(pool[0][0]))
        # print("pool[0][1] is "+str(pool[0][1]))
        if(pool[0][0] in YOU_path):
            inters_name=pool[0][0]
            break
        else:
            look_for=pool[0][1]
            #print("count increased")
            count+=1
        #SAN_path.add(look_for)
    else:
        break

#inters=[i for i in YOU_path & SAN_path]
#inters_name=inters[0]
print("Intersection is: "+inters_name)

#find num of orbits to intersection
look_for=YOU_orbit
while(True):
    pool=[i for i in ob_orbits if i[0] == look_for]
    if pool:
        if(pool[0][1]==inters_name):
            count+=1
            break
        else:
            count+=1
            #print("count increased")
            look_for=pool[0][1]
    else:
        print("An error occurred...")
        break

# look_for=SAN_orbit
# while(True):
#     pool=[i for i in ob_orbits if i[0] == look_for]
#     if pool:
#         if(pool[0][1]==inters_name):
#             break
#         else:
#             count+=1
#             look_for=pool[0][1]
#     else:
#         print("An error occurred...")
#         break

print("Minimum orbits number to reach Santa: "+ str(count))