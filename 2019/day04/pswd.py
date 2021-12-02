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
        if (num_str[idx]==num_str[idx+1]):
            double_exist=True
    if(double_exist==False):
        continue
    
    #second check
    for idx in range(0, len(num_str)-1):
        if (num_str[idx]>num_str[idx+1]):
            monotone=False
            break
    if(monotone==False):
        continue
    
    #third check
    # if(len(num_str)!=6):
    #     continue

    count+=1
    passwords.append(number)

print("Solution found: "+str(count))