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
for x in range(len(ob_names)):
    look_for=ob_names[x]
    while(True):
        # if(x==0):
        #     print("Looking for "+look_for)
        pool=[i for i in ob_orbits if i[0] == look_for]
        if pool:
            #print("Look up dimension is "+str(len(pool)))
            count+=1
            look_for=pool[0][1]
        else:
            break

print("Orbits number: "+ str(count))

print("Orbits number / set dimension: "+str(count/len(ob_orbits)))