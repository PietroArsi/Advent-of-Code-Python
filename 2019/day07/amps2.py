import itertools

f=open("i7.txt", "r")
memory=f.read().split(",")
f.close()

#index=0
input_comb=list(itertools.permutations(range(5, 10), 5))
output=0
max_output=-1
input_switch=False
count=0

numbers=[]
indexes=[]
checks=[]
finished=[]
input_vals=[]
for i in range(5):
    numbers.append(list(memory))

indexes=[0,0,0,0,0]

for i in range(5):
    checks.append(False)

finished=[False,False,False,False,False]

which_amp=0

for input in input_comb:
    count+=1
    which_amp=0
    output=0
    indexes=[0,0,0,0,0]
    numbers.clear()
    for i in range(5):
        numbers.append(list(memory))
    input_vals.clear()
    for char in input:
        input_vals.append(str(char))
    finished.clear()
    finished=[False,False,False,False,False]
    checks.clear()
    for i in range(5):
        checks.append(False)

    while(True):
        num=numbers[which_amp][indexes[which_amp]]

        num="00000"+num
        instruction=num[len(num)-2]+num[len(num)-1]
        mode1=num[len(num)-3]
        mode2=num[len(num)-4]

        if(instruction=="01"):
            if(mode1=="1"):
                num1=int(numbers[which_amp][indexes[which_amp]+1])
            elif(mode1=="0"):
                num1=int(numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])])
            if(mode2=="1"):
                num2=int(numbers[which_amp][indexes[which_amp]+2])
            elif(mode2=="0"):
                num2=int(numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+2])])

            numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+3])]=str(num1+num2)
            indexes[which_amp]+=4

        elif(instruction=="02"):
            if(mode1=="1"):
                num1=int(numbers[which_amp][indexes[which_amp]+1])
            elif(mode1=="0"):
                num1=int(numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])])
            if(mode2=="1"):
                num2=int(numbers[which_amp][indexes[which_amp]+2])
            elif(mode2=="0"):
                num2=int(numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+2])])

            #operation
            numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+3])]=str(num1*num2)
            indexes[which_amp]+=4
        elif(instruction=="03"):
            if(checks[which_amp]==False):
                checks[which_amp]=True
                val=input_vals[which_amp]
                numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])]=str(val)
            elif(checks[which_amp]==True):
                val=output
                numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])]=str(val)
            indexes[which_amp]+=2
        elif(instruction=="04"):
            if(mode1=="0"):
                output=numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])]
            elif(mode1=="1"):
                output=numbers[which_amp][indexes[which_amp]+1]
            indexes[which_amp]+=2

            next1=(which_amp+1)%5
            next2=(which_amp+2)%5
            next3=(which_amp+3)%5
            next4=(which_amp+4)%5
            if(finished[next1]==False):
                #print("1")
                which_amp=next1
            elif(finished[next2]==False):
                #print("2")
                which_amp=next2
            elif(finished[next3]==False):
                #print("3")
                which_amp=next3
            elif(finished[next4]==False):
                #print("4")
                which_amp=next4
            else:
                #print("fine")
                break

        elif(instruction=="05"):
            #print("Intruction 5")
            if(mode1=="0"):
                param1=numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])]
            elif(mode1=="1"):
                param1=numbers[which_amp][indexes[which_amp]+1]
            if(mode2=="0"):
                param2=numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+2])]
            elif(mode2=="1"):
                param2=numbers[which_amp][indexes[which_amp]+2]
            #check
            if(int(param1)!=0):
                indexes[which_amp]=int(param2)
            else:
                indexes[which_amp]+=3

        elif(instruction=="06"):
            #print("Instruction 6")
            if(mode1=="0"):
                param1=numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])]
            elif(mode1=="1"):
                param1=numbers[which_amp][indexes[which_amp]+1]
            if(mode2=="0"):
                param2=numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+2])]
            elif(mode2=="1"):
                param2=numbers[which_amp][indexes[which_amp]+2]
            #check
            if(int(param1)==0):

                indexes[which_amp]=int(param2)
            else:
                indexes[which_amp]+=3

        elif(instruction=="07"):
            #print("Instruction 7")
            if(mode1=="0"):
                param1=numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])]
            elif(mode1=="1"):
                param1=numbers[which_amp][indexes[which_amp]+1]
            if(mode2=="0"):
                param2=numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+2])]
            elif(mode2=="1"):
                param2=numbers[which_amp][indexes[which_amp]+2]
            #check
            if(int(param1)<int(param2)):
                numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+3])]=1
            else:
                numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+3])]=0

            indexes[which_amp]+=4

        elif(instruction=="08"):
            #print("Instruction 8")
            if(mode1=="0"):
                param1=numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])]
            elif(mode1=="1"):
                param1=numbers[which_amp][indexes[which_amp]+1]
            if(mode2=="0"):
                param2=numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+2])]
            elif(mode2=="1"):
                param2=numbers[which_amp][indexes[which_amp]+2]
            #check
            if(int(param1)==int(param2)):
                numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+3])]=1
            else:
                numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+3])]=0
            indexes[which_amp]+=4

        elif(instruction=="99"):
            finished[which_amp]=True
            next1=(which_amp+1)%5
            next2=(which_amp+2)%5
            next3=(which_amp+3)%5
            next4=(which_amp+4)%5
            if(finished[next1]==False):
                #print("991")
                which_amp=next1
            elif(finished[next2]==False):
                #print("992")
                which_amp=next2
            elif(finished[next3]==False):
                #print("993")
                which_amp=next3
            elif(finished[next4]==False):
               #print("994")
                which_amp=next4
            else:
                #print("fine")
                break
            
        else:
            print("An error occurred, number read is: "+num+" and index is: "+str(indexes[which_amp]))
            break
    if(int(output)>int(max_output) and int(output)>0):
        #print(input)
        max_output=output

print("Max output: "+str(max_output))