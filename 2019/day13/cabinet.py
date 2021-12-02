import array

f=open("inputs/i13.txt", "r")

numbers=f.read().split(",")
f.close()

#alloc more memory
memory_band=10000
start=len(numbers)
for x in range(start, memory_band-start):
    numbers.append("0")

painted_panels=list()
painted_white_panels=[]
robot_direction="up"
robot_position=(0,0)
color_to_paint=0
robot_movement="0"
provided_color=False

tile_grid=[]
block_count=0

index=0
relative_base=0
count_op4=0
while(True):
    num=numbers[index]

    num="000000"+num
    instruction=num[len(num)-2]+num[len(num)-1]
    mode1=num[len(num)-3]
    mode2=num[len(num)-4]
    mode3=num[len(num)-5]
    #print(instruction+" at index "+str(index))
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
        # val=input("Insert ID: ")
        if(mode1=="0"):
            if(0<=int(numbers[index+1])<memory_band):
                if(robot_position not in painted_white_panels):
                    numbers[int(numbers[index+1])]=str(0)
                    #f.write("ho letto casella nera\n")
                elif(robot_position in painted_white_panels):
                    numbers[int(numbers[index+1])]=str(1)
                    #f.write("ho letto casella bianca\n")
        elif(mode1=="2"):
            if(0<=int(numbers[index+1])+relative_base<memory_band):
                if(robot_position not in painted_white_panels):
                    numbers[int(numbers[index+1])+relative_base]==str(0)
                elif(robot_position in painted_white_panels):
                    numbers[int(numbers[index+1])+relative_base]==str(1)

        index+=2

    elif(instruction=="04"):
        count_op4+=1
        if(mode1=="0"):
            if(0<=int(numbers[index+1])<memory_band):
                #print("Diagnostic code: "+numbers[int(numbers[index+1])])
                output_val=numbers[int(numbers[index+1])]
            else:
                index+=2
                continue
        elif(mode1=="1"):
            if(0<=index+1<memory_band):
                #print("Diagnostic code: "+numbers[index+1])
                output_val=numbers[index+1]
            else:
                index+=2
                continue
        elif(mode1=="2"):
            if(0<=int(numbers[index+1])+relative_base<memory_band):
                #print("Diagnostic code: "+numbers[int(numbers[index+1])+relative_base])
                output_val=numbers[int(numbers[index+1])+relative_base]
            else:
                index+=2
                continue
        if(count_op4==1):
            x_value=int(output_val)
        elif(count_op4==2):
            y_value=int(output_val)
        elif(count_op4==3):
            count_op4=0
            tile_grid.append([int(y_value), int(x_value), int(output_val)])
            if(int(output_val)==2):
                block_count+=1

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
                numbers[int(numbers[index+3])]=str(1)
            else:
                numbers[int(numbers[index+3])]=str(0)
        elif(mode3=="2"):
            if(int(param1)<int(param2)):
                numbers[int(numbers[index+3])+relative_base]=str(1)
            else:
                numbers[int(numbers[index+3])+relative_base]=str(0)
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
                numbers[int(numbers[index+3])]=str(1)
            else:
                numbers[int(numbers[index+3])]=str(0)
        elif(mode3=="2"):
            if(int(param1)==int(param2)):
                numbers[int(numbers[index+3])+relative_base]=str(1)
            else:
                numbers[int(numbers[index+3])+relative_base]=str(0)
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

#f.close()
print("Number of blocks: "+str(block_count))