import array

f=open("i5.txt", "r")

numbers=f.read().split(",")
f.close()

index=0

while(True):
    num=numbers[index]

    # if(len(num)>1):
    #     intruction=num[len(num)-2]
    #     intruction+=num[len(num)-1]
    # else:
    #     intruction=num[len(num)-1]
    # index+=1

    num="00000"+num
    instruction=num[len(num)-2]+num[len(num)-1]
    mode1=num[len(num)-3]
    mode2=num[len(num)-4]
    # mode3=num[len(num)-5]
    #print(instruction)

    # if(index>20):
    #     break

    if(instruction=="01"):
        if(mode1=="1"):
            num1=int(numbers[index+1])
        elif(mode1=="0"):
            num1=int(numbers[int(numbers[index+1])])
        if(mode2=="1"):
            num2=int(numbers[index+2])
        elif(mode2=="0"):
            num2=int(numbers[int(numbers[index+2])])

        #operation
        #print("I have to add "+str(num1)+" and "+str(num2)+" and put the result in "+numbers[index+3])
        numbers[int(numbers[index+3])]=str(num1+num2)
        #print("Now it's "+numbers[int(numbers[index+3])])
        index+=4

    elif(instruction=="02"):
        if(mode1=="1"):
            num1=int(numbers[index+1])
        elif(mode1=="0"):
            num1=int(numbers[int(numbers[index+1])])
        if(mode2=="1"):
            num2=int(numbers[index+2])
        elif(mode2=="0"):
            num2=int(numbers[int(numbers[index+2])])
        #operation
        numbers[int(numbers[index+3])]=str(num1*num2)
        index+=4
    elif(instruction=="03"):
        val=input("Insert ID: ")
        numbers[int(numbers[index+1])]=str(val)
        index+=2
    elif(instruction=="04"):
        #print("Index is: "+str(index))
        if(numbers[index+2]=="99"):
            if(mode1=="0"):
                print("Diagnostic code: "+numbers[int(numbers[index+1])])
            elif(mode1=="1"):
                print("Diagnostic code: "+numbers[index+1])
        else:
            if(mode1=="0"):
                print("Test result: "+numbers[int(numbers[index+1])])
            elif(mode1=="1"):
                print("Test result: "+numbers[index+1])
        index+=2
    elif(instruction=="99"):
        break
    else:
        print("An error occurred")
        break