import array

f=open("i1.txt", "r")
mass= []
mass=f.readlines()
f.close()

partialsum=0
totalsum=0

for num in mass:
    if(num!="\n"):
        partialsum=int(int(num)/3-2)
        fuel_needed=partialsum
        while(fuel_needed>0):
            fuel_needed=int(fuel_needed/3-2)
            if(fuel_needed<0):
                fuel_needed=0
            partialsum+=fuel_needed
        totalsum+=partialsum


print(totalsum)