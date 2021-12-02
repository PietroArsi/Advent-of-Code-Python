import array

f=open("i2.txt", "r")

numbers=f.read().split(",")

rec=int(len(numbers)/4)+len(numbers)%4

numbers[1]=12
numbers[2]=2

for i in range(rec):
    cursor=i*4
    input1=int(numbers[cursor+1])
    input2=int(numbers[cursor+2])
    output=int(numbers[cursor+3])

    if(numbers[cursor]=="1"):
        numbers[output]=str(int(numbers[input1])+int(numbers[input2]))
    if(numbers[cursor]=="2"):
        numbers[output]=str(int(numbers[input1])*int(numbers[input2]))
    if(numbers[cursor]=="99"):
        break

print("Zero position happens to be "+numbers[0])