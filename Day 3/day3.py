from sys import platform
import numpy as np

file=open('./input.txt')
lines=file.readlines()


#First making trees to be 1 and path to be 0

tree_map=np.array([np.array(list(line.strip())) for line in lines ])
tree_map[np.where(tree_map=='#')]=1
tree_map[np.where(tree_map=='.')]=0
tree_map=tree_map.astype(int)


# calculate the length of map required to be repeated in order to have the line extend till end
slope=1/3


h,w=tree_map.shape
width_required= h/slope
repeats_about_width=np.ceil(width_required/w).astype(int)

#repeat the map along the width
tree_map=np.tile(tree_map,repeats_about_width)


#Now that the map is big enough for us to draw a line, draw a line on an empty map first


h,w=tree_map.shape

x=np.linspace(0,w-1,w)
y=np.linspace(0,h-1,h)

xx,yy=np.meshgrid(x,y)


print(np.sum(tree_map[np.where(  np.abs(yy/xx - slope)<1e-10 )]))  ## Add those points in the map which have thier slope-slope required close to zero(since division may not be exact, we do not try == slope)





### Part 2

z=1.0  # use float, integer will cause probelms with limited memory
for slope in [1,1/3,1/5,1/7,2]:

    h,w=tree_map.shape
    width_required= h/slope
    repeats_about_width=np.ceil(width_required/w).astype(int)

    #repeat the map along the width
    tree_map=np.tile(tree_map,repeats_about_width)


    #Now that the map is big enough for us to draw a line, draw a line on an empty map first


    h,w=tree_map.shape

    x=np.linspace(0,w-1,w)
    y=np.linspace(0,h-1,h)

    xx,yy=np.meshgrid(x,y)


    num=(np.sum(tree_map[np.where(  np.abs(yy/xx - slope)<1e-10 )]))  ## Add those points in the map which have thier slope-slope required close to zero(since division may not be exact, we do not try == slope)
    print(num)
    z=z*num
print(z)

