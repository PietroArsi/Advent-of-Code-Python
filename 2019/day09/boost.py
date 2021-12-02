import array

f=open("inputs/i9.txt", "r")

numbers=f.read().split(",")
f.close()

#alloc more memory
memory_band=10000
start=len(numbers)
for x in range(start, memory_band-start):
    numbers.append("0")

# print(str(numbers))

index=0
relative_base=0

while(True):
    num=numbers[index]

    num="000000"+num
    instruction=num[len(num)-2]+num[len(num)-1]
    mode1=num[len(num)-3]
    mode2=num[len(num)-4]
    mode3=num[len(num)-5]
    # print(instruction)
    if(instruction=="01"):
        if(mode1=="1"):
            if(0<=index+1<memory_band):
                num1=int(numbers[index+1])
            else:
                index+=4
                continue
        elif(mode1=="0"):
            # print("aaa "+str(index+1))
            if(0<=int(numbers[index+1])<memory_band):
                num1=int(numbers[int(numbers[index+1])])
            else:
                index+=4
                continue
        elif(mode1=="2"):
            if(0<=int(numbers[index+1])+relative_base<memory_band):
                num1=int(numbers[int(numbers[index+1])+relative_base])
            else:
                index+=4
                continue
        if(mode2=="1"):
            if(0<=index+2<memory_band):
                num2=int(numbers[index+2])
            else:
                index+=4
                continue
        elif(mode2=="0"):
            if(0<=int(numbers[index+2])<memory_band):
                num2=int(numbers[int(numbers[index+2])])
            else:
                index+=4
                continue
        elif(mode2=="2"):
            if(0<=int(numbers[index+2])+relative_base<memory_band):
                num2=int(numbers[int(numbers[index+2])+relative_base])
            else:
                index+=4
                continue

        #operation
        if(mode3=="0"):
            numbers[int(numbers[index+3])]=str(num1+num2)
        elif(mode3=="2"):
            numbers[int(numbers[index+3])+relative_base]=str(num1+num2)
        index+=4

    elif(instruction=="02"):
        if(mode1=="1"):
            if(0<=index+1<memory_band):
                num1=int(numbers[index+1])
            else:
                index+=4
                continue
        elif(mode1=="0"):
            if(0<=int(numbers[index+1])<memory_band):
                num1=int(numbers[int(numbers[index+1])])
            else:
                index+=4
                continue
        elif(mode1=="2"):
            if(0<=int(numbers[index+1])+relative_base<memory_band):
                num1=int(numbers[int(numbers[index+1])+relative_base])
            else:
                index+=4
                continue
        if(mode2=="1"):
            if(0<=index+2<memory_band):
                num2=int(numbers[index+2])
            else:
                index+=4
                continue
        elif(mode2=="0"):
            if(0<=int(numbers[index+2])<memory_band):
                num2=int(numbers[int(numbers[index+2])])
            else:
                index+=4
                continue
        elif(mode2=="2"):
            if(0<=int(numbers[index+2])+relative_base<memory_band):
                num2=int(numbers[int(numbers[index+2])+relative_base])
            else:
                index+=4
                continue
        #operation
        if(mode3=="0"):
            numbers[int(numbers[index+3])]=str(num1*num2)
        elif(mode3=="2"):
            numbers[int(numbers[index+3])+relative_base]=str(num1*num2)
        index+=4
    elif(instruction=="03"):
        val=input("Insert ID: ")
        if(mode1=="0"):
            if(0<=int(numbers[index+1])<memory_band):
                numbers[int(numbers[index+1])]=str(val)
            else:
                index+=2
                continue
        elif(mode1=="2"):
            if(0<=int(numbers[index+1])+relative_base<memory_band):
                numbers[int(numbers[index+1])+relative_base]=str(val)
            else:
                index+=2
                continue
        index+=2

    elif(instruction=="04"):
        #print("Rel val: "+str(relative_base))
        if(numbers[index+2]=="99"):
            if(mode1=="0"):
                if(0<=int(numbers[index+1])<memory_band):
                    print("Diagnostic code: "+numbers[int(numbers[index+1])])
                else:
                    index+=2
                    continue
            elif(mode1=="1"):
                if(0<=index+1<memory_band):
                    print("Diagnostic code: "+numbers[index+1])
                else:
                    index+=2
                    continue
            elif(mode1=="2"):
                if(0<=int(numbers[index+1])+relative_base<memory_band):
                    print("Diagnostic code: "+numbers[int(numbers[index+1])+relative_base])
                else:
                    index+=2
                    continue
        else:
            #print("aaa")
            if(mode1=="0"):
                if(0<=int(numbers[index+1])<memory_band):
                    print("Test result: "+numbers[int(numbers[index+1])])
                else:
                    index+=2
                    continue
            elif(mode1=="1"):
                if(0<=index+1<memory_band):
                    print("Test result: "+numbers[index+1])
                else:
                    index+=2
                    continue
            elif(mode1=="2"):
                if(0<=int(numbers[index+1])+relative_base<memory_band):
                    print("Test result: "+numbers[int(numbers[index+1])+relative_base])
                else:
                    index+=2
                    continue

        index+=2
    elif(instruction=="05"):
        if(mode1=="0"):
            if(0<=int(numbers[index+1])<memory_band):
                param1=numbers[int(numbers[index+1])]
            else:
                index+=3
                continue
        elif(mode1=="1"):
            if(0<=index+1<memory_band):
                param1=numbers[index+1]
            else:
                index+=3
                continue
        elif(mode1=="2"):
            if(0<=int(numbers[index+1])+relative_base<memory_band):
                param1=numbers[int(numbers[index+1])+relative_base]
            else:
                index+=3
                continue
        if(mode2=="0"):
            if(0<=int(numbers[index+2])<memory_band):
                param2=numbers[int(numbers[index+2])]
            else:
                index+=3
                continue
        elif(mode2=="1"):
            if(0<=index+2<memory_band):
                param2=numbers[index+2]
            else:
                index+=3
                continue
        elif(mode2=="2"):
            if(0<=int(numbers[index+2])+relative_base<memory_band):
                param2=numbers[int(numbers[index+2])+relative_base]
            else:
                index+=3
                continue
        #check
        if(int(param1)!=0):
            index=int(param2)
        else:
            index+=3

    elif(instruction=="06"):
        if(mode1=="0"):
            if(0<=int(numbers[index+1])<memory_band):
                param1=numbers[int(numbers[index+1])]
            else:
                index+=3
                continue
        elif(mode1=="1"):
            if(0<=index+1<memory_band):
                param1=numbers[index+1]
            else:
                index+=3
                continue
        elif(mode1=="2"):
            if(0<=int(numbers[index+1])+relative_base<memory_band):
                param1=numbers[int(numbers[index+1])+relative_base]
            else:
                index+=3
                continue
        if(mode2=="0"):
            if(0<=int(numbers[index+2])<memory_band):
                param2=numbers[int(numbers[index+2])]
            else:
                index+=3
                continue
        elif(mode2=="1"):
            if(0<=index+2<memory_band):
                param2=numbers[index+2]
            else:
                index+=3
                continue
        elif(mode2=="2"):
            if(0<=int(numbers[index+2])+relative_base<memory_band):
                param2=numbers[int(numbers[index+2])+relative_base]
            else:
                index+=3
                continue
        #check
        if(int(param1)==0):
            index=int(param2)
        else:
            index+=3

    elif(instruction=="07"):
        if(mode1=="0"):
            if(0<=int(numbers[index+1])<memory_band):
                param1=numbers[int(numbers[index+1])]
            else:
                index+=4
                continue
        elif(mode1=="1"):
            if(0<=index+1<memory_band):
                param1=numbers[index+1]
            else:
                index+=4
                continue
        elif(mode1=="2"):
            if(0<=int(numbers[index+1])+relative_base<memory_band):
                param1=numbers[int(numbers[index+1])+relative_base]
            else:
                index+=4
                continue
        if(mode2=="0"):
            if(0<=int(numbers[index+2])<memory_band):
                param2=numbers[int(numbers[index+2])]
            else:
                index+=4
                continue
        elif(mode2=="1"):
            if(0<=index+2<memory_band):
                param2=numbers[index+2]
            else:
                index+=4
                continue
        elif(mode2=="2"):
            if(0<=int(numbers[index+2])+relative_base<memory_band):
                param2=numbers[int(numbers[index+2])+relative_base]
            else:
                index+=4
                continue
        #check
        if(mode3=="0"):
            if(int(param1)<int(param2)):
                numbers[int(numbers[index+3])]=1
            else:
                numbers[int(numbers[index+3])]=0
        elif(mode3=="2"):
            if(int(param1)<int(param2)):
                numbers[int(numbers[index+3])+relative_base]=1
            else:
                numbers[int(numbers[index+3])+relative_base]=0
        index+=4

    elif(instruction=="08"):
        if(mode1=="0"):
            if(0<=int(numbers[index+1])<memory_band):
                param1=numbers[int(numbers[index+1])]
            else:
                index+=4
                continue
        elif(mode1=="1"):
            if(0<=index+1<memory_band):
                param1=numbers[index+1]
            else:
                index+=4
                continue
        elif(mode1=="2"):
            if(0<=int(numbers[index+1])+relative_base<memory_band):
                param1=numbers[int(numbers[index+1])+relative_base]
            else:
                index+=4
                continue
        if(mode2=="0"):
            if(0<=int(numbers[index+2])<memory_band):
                param2=numbers[int(numbers[index+2])]
            else:
                index+=4
                continue
        elif(mode2=="1"):
            if(0<=index+2<memory_band):
                param2=numbers[index+2]
            else:
                index+=4
                continue
        elif(mode2=="2"):
            if(0<=int(numbers[index+2])+relative_base<memory_band):
                param2=numbers[int(numbers[index+2])+relative_base]
            else:
                index+=4
                continue
        #check
        if(mode3=="0"):
            if(int(param1)==int(param2)):
                numbers[int(numbers[index+3])]=1
            else:
                numbers[int(numbers[index+3])]=0
        elif(mode3=="2"):
            if(int(param1)==int(param2)):
                numbers[int(numbers[index+3])+relative_base]=1
            else:
                numbers[int(numbers[index+3])+relative_base]=0
        index+=4
    
    elif(instruction=="09"):
        if(mode1=="0"):
            if(0<=int(numbers[index+1])<memory_band):
                param1=numbers[int(numbers[index+1])]
            else:
                index+=2
                continue
        elif(mode1=="1"):
            if(0<=index+1<memory_band):
                param1=numbers[index+1]
            else:
                index+=2
                continue
        elif(mode1=="2"):
            if(0<=int(numbers[index+1])+relative_base<memory_band):
                param1=numbers[int(numbers[index+1])+relative_base]
            else:
                index+=2
                continue
        relative_base+=int(param1)
        index+=2

    elif(instruction=="99"):
        break
    else:
        print("An error occurred, number read is: "+num+" and index is: "+str(index))
        break