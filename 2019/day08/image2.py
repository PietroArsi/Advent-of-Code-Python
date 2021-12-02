

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

matrix=[[0 for i in range(tall)]for i in range(large)]

f=open("message.txt", "w")
for i in image:
    f.write(str(i)+"\n")
f.close()

f=open("message.txt", "w")
for y in range(tall):
    for x in range(large):
        for layer in range(len(image)):
            if(image[layer][y][x]=="0"):
                f.write(" ")
                break
            elif(image[layer][y][x]=="1"):
                f.write("o")
                print(u'\u2588'.encode('utf-8'))
                break
    f.write("\n")

# f=open("message.txt", "w")
# for x in matrix:
#     f.write(str(i)+"\n")
# f.close()        