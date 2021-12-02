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

# for i in input_comb:
#     print(i)
numbers=[]
indexes=[]
checks=[]
finished=[]
input_vals=[]
for i in range(5):
    numbers.append(list(memory))

# for i in numbers:
#     print(str(i))
# print("--------")
# numbers[1][3]=str(12345)
# for i in numbers:
#     print(str(i))

indexes=[0,0,0,0,0]

for i in range(5):
    checks.append(False)

# for i in range(5):
#     finished.append(False)
finished=[False,False,False,False,False]

which_amp=0

for input in input_comb:
    #print("Combinazione "+str(count+1)+" su "+str(len(input_comb)))
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
    # for x in range(5):
    #     finished.append(False)
    finished=[False,False,False,False,False]
    checks.clear()
    for i in range(5):
        checks.append(False)


    #input_switch=False
    #for i in input:
    #count+=1
    #index=indexes[0]
    # bp=100
    # if(count>bp):
    #     break
    while(True):
        # if(count>bp):
        #     break
        
        # f=open("output7.2.txt", "a")
        # f.write("\n")
        # for c in numbers:
        #     f.write(str(count)+"\n"+str(c)+"\n")
        # f.close()


        num=numbers[which_amp][indexes[which_amp]]

        num="00000"+num
        instruction=num[len(num)-2]+num[len(num)-1]
        mode1=num[len(num)-3]
        mode2=num[len(num)-4]
        #print(instruction)

        # if(index>20):
        #     break

        if(instruction=="01"):
            if(mode1=="1"):
                num1=int(numbers[which_amp][indexes[which_amp]+1])
            elif(mode1=="0"):
                num1=int(numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])])
            if(mode2=="1"):
                num2=int(numbers[which_amp][indexes[which_amp]+2])
            elif(mode2=="0"):
                num2=int(numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+2])])

            #print(str(numbers[which_amp]))
            #print(str(num1)+" + "+str(num2)+" = "+str(num1+num2))
            #operation
            #print("I have to add "+str(num1)+" and "+str(num2)+" and put the result in "+numbers[index+3])
            numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+3])]=str(num1+num2)
            #print("1-Scrivo in posizione "+numbers[which_amp][indexes[which_amp]+3])
            # f=open("terminale.txt","a")
            # f.write("Modifico "+str(which_amp)+"\n")
            # f.write("Finished: "+str(finished)+"\n")
            # for i in numbers:
            #     f.write(str(i)+"\n")
            # f.write("--------\n")
            #print("Now it's "+numbers[int(numbers[index+3])])
            #print("1-Phase #"+str(which_amp)+", index: "+str(indexes[which_amp]))
            indexes[which_amp]+=4
            #print("1-Phase #"+str(which_amp)+", now index: "+str(indexes[which_amp]))

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
            #print("index is: "+str(indexes[which_amp]))
            #print(str(numbers[which_amp]))
            numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+3])]=str(num1*num2)
            #print("2-Scrivo in posizione "+numbers[which_amp][indexes[which_amp]+3])
            #print(str(numbers[which_amp]))
            #print("2-Phase #"+str(which_amp)+", index: "+str(indexes[which_amp]))
            indexes[which_amp]+=4
            # f=open("terminale.txt","a")
            # f.write("Modifico "+str(which_amp)+"\n")
            # f.write("Finished: "+str(finished)+"\n")
            # for i in numbers:
            #     f.write(str(i)+"\n")
            # f.write("--------\n")
            #print("2-Phase #"+str(which_amp)+", now index: "+str(indexes[which_amp]))
        elif(instruction=="03"):
            #val=input("Insert ID: ")
            if(checks[which_amp]==False):
                checks[which_amp]=True
                val=input_vals[which_amp]
                #print("Phase "+str(which_amp)+" initialized")
                #print(str(numbers[which_amp]))
                numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])]=str(val)
            elif(checks[which_amp]==True):
                val=output
                #print("Phase "+str(which_amp)+", input received: "+str(val))
                #print(str(numbers[which_amp]))
                #print(numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])])
                numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])]=str(val)
            #print("3-Scrivo l'input in posizione "+numbers[which_amp][indexes[which_amp]+1])
            #print(str(numbers[which_amp]))
            #print("Phase #"+str(which_amp)+", index: "+str(indexes[which_amp]))
            indexes[which_amp]+=2
            # f=open("terminale.txt","a")
            # f.write("Modifico "+str(which_amp)+"\n")
            # f.write("Finished: "+str(finished)+"\n")
            # for i in numbers:
            #     f.write(str(i)+"\n")
            # f.write("--------\n")
            #print("Phase #"+str(which_amp)+", now index: "+str(indexes[which_amp]))
        elif(instruction=="04"):
            if(mode1=="0"):
                output=numbers[which_amp][int(numbers[which_amp][indexes[which_amp]+1])]
            elif(mode1=="1"):
                output=numbers[which_amp][indexes[which_amp]+1]
            # output=outp
            #print("Amp: "+str(which_amp)+", output written: "+output)
            #print("Phase #"+str(which_amp)+", index: "+str(indexes[which_amp]))
            indexes[which_amp]+=2
            #print("Phase #"+str(which_amp)+", now index: "+str(indexes[which_amp]))

            next1=(which_amp+1)%5
            next2=(which_amp+2)%5
            next3=(which_amp+3)%5
            next4=(which_amp+4)%5
            #print("Amp #"+str(which_amp))
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

            #print("Amp # "+str(which_amp))
            # f=open("terminale.txt","a")
            # f.write("Modifico "+str(which_amp)+"\n")
            # f.write("Finished: "+str(finished)+"\n")
            # for i in numbers:
            #     f.write(str(i)+"\n")
            # f.write("--------\n")

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
            #print(str(numbers[which_amp]))
            #print("Leggo "+param1+" con mode "+mode1)
            if(int(param1)!=0):
                indexes[which_amp]=int(param2)
            else:
                indexes[which_amp]+=3

            # f=open("terminale.txt","a")
            # f.write("Modifico "+str(which_amp)+"\n")
            # f.write("Finished: "+str(finished)+"\n")
            # for i in numbers:
            #     f.write(str(i)+"\n")
            # f.write("--------\n")

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
            #print("Leggo "+param1+" con mode "+mode1)
            if(int(param1)==0):

                indexes[which_amp]=int(param2)
            else:
                indexes[which_amp]+=3

            # f=open("terminale.txt","a")
            # f.write("Modifico "+str(which_amp)+"\n")
            # f.write("Finished: "+str(finished)+"\n")
            # for i in numbers:
            #     f.write(str(i)+"\n")
            # f.write("--------\n")

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

            #print("Phase #"+str(which_amp)+", index: "+str(indexes[which_amp]))
            indexes[which_amp]+=4

            # f=open("terminale.txt","a")
            # f.write("Modifico "+str(which_amp)+"\n")
            # f.write("Finished: "+str(finished)+"\n")
            # for i in numbers:
            #     f.write(str(i)+"\n")
            # f.write("--------\n")
            #print("Phase #"+str(which_amp)+", now index: "+str(indexes[which_amp]))

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
            #print("Phase #"+str(which_amp)+", index: "+str(indexes[which_amp]))
            indexes[which_amp]+=4

            # f=open("terminale.txt","a")
            # f.write("Modifico "+str(which_amp)+"\n")
            # f.write("Finished: "+str(finished)+"\n")
            # for i in numbers:
            #     f.write(str(i)+"\n")
            # f.write("--------\n")
            #print("Phase #"+str(which_amp)+", now index: "+str(indexes[which_amp]))

        elif(instruction=="99"):
            finished[which_amp]=True
            #print("Phase "+str(which_amp)+" finished! Index is "+str(indexes[which_amp]))
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
            # f=open("terminale.txt","a")
            # f.write("Modifico "+str(which_amp)+"\n")
            # f.write("Finished: "+str(finished)+"\n")
            # for i in numbers:
            #     f.write(str(i)+"\n")
            # f.write("--------\n")
        else:
            print("An error occurred, number read is: "+num+" and index is: "+str(indexes[which_amp]))
            break
    if(int(output)>int(max_output) and int(output)>0):
        #print(input)
        max_output=output

print("Max output: "+str(max_output))