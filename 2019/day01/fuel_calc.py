import array

f=open("i1.txt", "r")
mass= []
mass=f.readlines()
f.close()

totalsum=0

for num in mass:
    if(num!="\n"):
        totalsum=totalsum + int((int(num)/3)-2)
        #print(num)

print(totalsum)