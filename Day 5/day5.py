import numpy as np

file=open('./input.txt')
lines=file.readlines()

ids=[]
for line in lines:
    # p1=line.strip()[:7]
    # p1=p1.replace('F','0')
    # p1=p1.replace('B','1')
    
    # #row_number=int(p1,2)

    # p2=line.strip()[7:]
    # p2=p2.replace('L','0')
    # p2=p2.replace('R','1')
    # #col_number=int(p2,2)
    #seat_id=row_number*8+col_number
    
    p=line
    p=p.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
    seat_id=int(p,2)
    
    ids.append(seat_id)

print(np.array(ids).max())
ids=np.sort(ids)

#part 2

idx=np.where((ids-np.roll(ids,1)==2))[0][0]

print(ids[idx-3:idx+3])