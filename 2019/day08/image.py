f=open("i8.txt", "r")
numbers=f.read()
f.close()
pixels=[]
for x in range(len(numbers)):
    pixels.append(numbers[x])

image=[]
large=25
tall=6

line_count=0
tall_count=0
a=0
b=large

for x in range(int(len(pixels)/(large*tall))):
    image.append([])
    tall_count=0
    while(tall_count<tall):
        image[line_count].append(list(pixels[a:b]))
        a+=large
        b+=large
        tall_count+=1
    line_count+=1

#image created
#now count zeroes

#print(str(image[0][0]))

zcount=0
# minzcount=0

for layer in range(0, len(image)):
    zcount=0
    for x in range(0, len(image[layer])):
        for y in range(0, len(image[layer][x])):
            if(image[layer][x][y]=="0"):
                zcount+=1
    if("minzcount" not in locals() and "bestlayer" not in locals()):
        minzcount=zcount
        bestlayer=layer
    else:
        if(zcount<minzcount):
            #print("aaa")
            minzcount=zcount
            bestlayer=layer

if(minzcount>0):
    print("Bestlayer is: "+str(bestlayer)+" with "+str(minzcount)+" zero(es)")
else:
    print("Error")

count1=0
count2=0
for x in range(0, tall):
    for y in range(0, large):
        if(image[bestlayer][x][y]=="1"):
            count1+=1
        elif(image[bestlayer][x][y]=="2"):
            count2+=1
        
print("Solution is: "+str(count1*count2))