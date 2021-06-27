import numpy as np

file=open('./input.txt')
lines=file.readlines();
nums=[int(num.strip()) for num in lines]


# PArt 1

for a in nums:
    for b in nums:
        if a+b==2020:
            print(a*b)

# part2

for a in nums:
    for b in nums:
        for c in nums:
            if a+b+c==2020:
                print(a*b*c)