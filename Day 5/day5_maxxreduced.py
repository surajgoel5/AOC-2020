with open('./input.txt') as file:
    ids=[int(line.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2) for line in file.readlines()]
    ids.sort()
    print(ids[-1])
   
    #part 2
    for i in range(1,len(ids)):
        if (ids[i]-ids[i-1])==2 :
            break 
    print(ids[i]-1)
