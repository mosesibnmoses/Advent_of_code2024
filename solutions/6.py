import numpy as np

from utils.helpers import parse_input, read_grid

#map=read_grid('../tests/6_test_input.txt')
map=read_grid('../data/6_input.txt')

print(map)

guard_coords=(np.where(map=="^")[0],np.where(map=="^")[1])

print(map)
turn={"^":">",">":"v","v":"<","<":"^"}

def calculate_next_coords(dir,coords):
    if dir=="^":
        print ('step up')
        return coords[0]-1,coords[1]
    if dir=="v":
        print ('step down')
        return coords[0]+1,coords[1]
    if dir==">":
        print ('step right')
        return coords[0],coords[1]+1
    if dir=="<":
        print ('step left')
        return coords[0],coords[1]-1

def update_map(dir,old_coords):
    new_coords=calculate_next_coords(dir,old_coords)
    #print ("next step contains",map[new_coords])
    if 0 <= new_coords[0] < len(map) and 0 <= new_coords[1] < len(map[0]):
        if map[new_coords]=="." or map[new_coords]=="X":
            map[old_coords]="X"
            map[new_coords]=dir
        if map[new_coords]=='#':
            print ("turning, was going",dir[0])
            print("now going",turn[dir[0]])
            dir=turn[dir[0]]
            new_coords=old_coords
            map[new_coords] = dir
    else:
        print ("LEFT THE MAP")
        return "X",old_coords
    return dir,new_coords

while True:
    dir,guard_coords=update_map(map[guard_coords],guard_coords)
    if dir=='X':
        map[guard_coords]="X"
        break
    print (dir, guard_coords)
print (np.sum(map=="X"))

