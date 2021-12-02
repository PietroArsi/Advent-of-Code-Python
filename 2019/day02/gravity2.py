import array

f=open("i2.txt", "r")
numbers=f.read().split(",")
f.close()
f=open("i2.txt", "r")
memory=f.read().split(",")
f.close()

f.close()

def reset_memory(nums=[]):
    #print("lens: "+str(len(nums))+" "+str(len(numbers)))
    for x in range(0, len(numbers)):
        nums[x]=numbers[x]

rec=int(len(numbers)/4)+len(numbers)%4

for noun in range(0,100):
    for verb in range(0,100):
        reset_memory(memory)
        memory[1]=str(noun)
        memory[2]=str(verb)
        #print(str(noun)+" "+str(verb))
        for i in range(rec):
            cursor=i*4
            # print(str(noun)+" "+str(verb))
            input1=int(memory[cursor+1])
            input2=int(memory[cursor+2])
            output=int(memory[cursor+3])

            if(memory[cursor]=="1"):
                memory[output]=str(int(memory[input1])+int(memory[input2]))
            if(memory[cursor]=="2"):
                memory[output]=str(int(memory[input1])*int(memory[input2]))
            if(memory[cursor]=="99"):
                break
        if(memory[0]=="19690720"):
            print("The answer is: "+str(100*noun+verb))
            break
            
print("End.")