import numpy as np

file=open('./input.txt')
contents=file.read()

groups=contents.split('\n\n')

#Part1
count=0
for group in groups:
    group=group.strip().replace('\n','')
    group_set=set(group)
    count+=len(group_set)

print(count)

#Part2

count=0
for group in groups:
    people=group.strip().split('\n')
    intersection_set=set('qwertyuiopasdfghjklzxcvbnm')
    for person in people:
        intersection_set=intersection_set.intersection(set(person))
    
    count+=len(intersection_set)

print(count)