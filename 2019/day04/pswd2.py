f=open("i4.txt", "r")
numbers=f.read().split("-")
f.close()

start=int(numbers[0])
finish=int(numbers[1])
# print(str(start)+" "+str(finish))

count=0
passwords=[]

for number in range(start, finish+1):
    num_str=str(number)
    double_exist=False
    monotone=True

    #first check
    for idx in range(0, len(num_str)-1):
        #print(str(idx))
        # if (num_str[idx]==num_str[idx+1]):
        #     if(idx>=4 or num_str[idx+2]!=num_str[idx]):
        #         if(idx==0 or num_str[idx-1]!=num_str[idx]):
        #             double_exist=True
        if(idx==0 and num_str[idx]==num_str[idx+1]!=num_str[idx+2]):
            double_exist=True
        elif(idx>0 and idx<4 and num_str[idx-1]!=num_str[idx]==num_str[idx+1]!=num_str[idx+2]):
            double_exist=True
        elif(idx>0 and idx>3 and num_str[idx-1]!=num_str[idx]==num_str[idx+1]):
            double_exist=True

    if(double_exist==False):
        continue
    
    #second check
    for idx in range(0, len(num_str)-1):
        if(num_str=="446783"):
            print("Is "+num_str[idx]+" greater than "+num_str[idx+1]+"?")

        if (int(num_str[idx])>int(num_str[idx+1])):
            if(num_str=="446783"):
                print("yes!")
            monotone=False
            break
        else:
            if(num_str=="446783"):
                print("no")

    if(monotone==False):
        continue
    
    #third check
    # if(len(num_str)!=6):
    #     continue

    count+=1
    passwords.append(number)

print("Solution found: "+str(count))
f=open("4.2.txt", "w")
for password in passwords:
    f.write(str(password)+"\n")
f.close()