import itertools

f=open("i7.txt", "r")
memory=f.read().split(",")
f.close()

index=0

input_comb=list(itertools.permutations(range(5), 5))
output=0
max_output=-1
input_switch=False
count=0

# for i in input_comb:
#     print(i)

for input in input_comb:
    output=0
    for i in input:
        count+=1
        input_switch=False
        numbers=memory.copy()
        index=0
        while(True):
            num=numbers[index]

            num="00000"+num
            instruction=num[len(num)-2]+num[len(num)-1]
            mode1=num[len(num)-3]
            mode2=num[len(num)-4]
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
                #val=input("Insert ID: ")
                if(input_switch==False):
                    input_switch=True
                    val=i
                    print("Phase "+str(val)+" initialized")
                    numbers[int(numbers[index+1])]=str(val)
                elif(input_switch==True):
                    val=output
                    print("Phase "+str(i)+", input received: "+str(val))
                    numbers[int(numbers[index+1])]=str(val)
                index+=2
            elif(instruction=="04"):
                #print("Index is: "+str(index))
                # if(numbers[index+2]=="99"):
                #     if(mode1=="0"):
                #         print("Diagnostic code: "+numbers[int(numbers[index+1])])
                #     elif(mode1=="1"):
                #         print("Diagnostic code: "+numbers[index+1])
                # else:
                #     if(mode1=="0"):
                #         print("Test result: "+numbers[int(numbers[index+1])])
                #     elif(mode1=="1"):
                #         print("Test result: "+numbers[index+1])

                if(mode1=="0"):
                    outp=numbers[int(numbers[index+1])]
                elif(mode1=="1"):
                    outp=numbers[index+1]
                output=outp
                print("Phase: "+str(i)+", output written: "+outp)
                index+=2

            elif(instruction=="05"):
                if(mode1=="0"):
                    param1=numbers[int(numbers[index+1])]
                elif(mode1=="1"):
                    param1=numbers[index+1]
                if(mode2=="0"):
                    param2=numbers[int(numbers[index+2])]
                elif(mode2=="1"):
                    param2=numbers[index+2]
                #check
                if(int(param1)!=0):
                    index=int(param2)
                else:
                    index+=3

            elif(instruction=="06"):
                if(mode1=="0"):
                    param1=numbers[int(numbers[index+1])]
                elif(mode1=="1"):
                    param1=numbers[index+1]
                if(mode2=="0"):
                    param2=numbers[int(numbers[index+2])]
                elif(mode2=="1"):
                    param2=numbers[index+2]
                #check
                if(int(param1)==0):
                    index=int(param2)
                else:
                    index+=3

            elif(instruction=="07"):
                if(mode1=="0"):
                    param1=numbers[int(numbers[index+1])]
                elif(mode1=="1"):
                    param1=numbers[index+1]
                if(mode2=="0"):
                    param2=numbers[int(numbers[index+2])]
                elif(mode2=="1"):
                    param2=numbers[index+2]
                #check
                if(int(param1)<int(param2)):
                    numbers[int(numbers[index+3])]=1
                else:
                    numbers[int(numbers[index+3])]=0
                index+=4

            elif(instruction=="08"):
                if(mode1=="0"):
                    param1=numbers[int(numbers[index+1])]
                elif(mode1=="1"):
                    param1=numbers[index+1]
                if(mode2=="0"):
                    param2=numbers[int(numbers[index+2])]
                elif(mode2=="1"):
                    param2=numbers[index+2]
                #check
                if(int(param1)==int(param2)):
                    numbers[int(numbers[index+3])]=1
                else:
                    numbers[int(numbers[index+3])]=0
                index+=4

            elif(instruction=="99"):
                break
            else:
                print("An error occurred, number read is: "+num+" and index is: "+str(index))
                break
    if(int(output)>int(max_output) and int(output)>0):
        print(input)
        max_output=output

print("Max output: "+str(max_output))