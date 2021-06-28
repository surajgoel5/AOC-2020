import numpy as np

file=open('./input.txt')
lines=file.readlines()

ids=[]
for line in lines:
    p1=line.strip()[:7]
    p1=[0 if c == 'F' else 1 for c in p1]

    row_number=0
    for i, bin_digit in enumerate(p1[::-1]):
        row_number+= bin_digit*(2**i)

  # print(row_number)


    p2=line.strip()[7:]
    p2=[0 if c == 'L' else 1 for c in p2]

    col_number=0
    for i, bin_digit in enumerate(p2[::-1]):
        col_number+= bin_digit*(2**i)
        
   # print(col_number)

    seat_id=row_number*8+col_number
    ids.append(seat_id)
print(np.array(ids).max())
ids=np.sort(ids)

#part 2

idx=np.where((ids-np.roll(ids,1)==2))[0][0]

print(ids[idx-3:idx+3])