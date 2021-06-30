from typing import Container
import numpy as np

file=open('./input.txt')
lines=file.readlines()


bags={}

for line in lines:
    container, contents=line.strip().replace('.','').split('contain')
    container=container.strip().replace('bags','').replace('bag','').strip()
    contents=contents.replace('.','').split(',')
    bags[container]=[]
    for content in contents:
        content=content.strip().split()
        if content[0]=='no':
            pass
        else:
            num=int(content[0])
            bags[container].append( content[1]+' '+content[2])
    
#for bag in bags: print(1,bag,1)

def search_for(main_bag,last_bag):
    #print(main_bag)
    if last_bag in bags[main_bag]:
        return True
    else:
        for bag in bags[main_bag]:
            if search_for(bag, last_bag):
                return True
        return False

count=0
for main_bag in bags:
    
    count+=search_for(main_bag,'shiny gold')
print(count)
  #  print(container,contents)
    #print(line)



#Part 2


bags={}

for line in lines:
    container, contents=line.strip().replace('.','').split('contain')
    container=container.strip().replace('bags','').replace('bag','').strip()
    contents=contents.replace('.','').split(',')
    bags[container]=[]
    for content in contents:
        content=content.strip().split()
        if content[0]=='no':
            pass
        else:
            num=int(content[0])
            bags[container].append( [num,content[1]+' '+content[2]])
    
#for bag in bags: print(1,bag,1)

def count_bags(main_bag):
    if len(bags[main_bag])==0:
        return 0
    else:
        count=0
        for num,bag in bags[main_bag]:
            count+=num*count_bags(bag) +num
        return count
print(count_bags('shiny gold'))
