import numpy as np

from utils.helpers import read_grid

filename= "../data/4_input.txt"

grid=read_grid(filename)
testgrid=read_grid("../tests/4_test_input.txt")

pattern1 = 'XMAS'
pattern2 = np.array([
        ['M', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'S']])
rows, cols = grid.shape

def check_direction(gridname,start_row,start_col,dir_row,dir_col):
    for i in range(len(pattern1)):
        r, c = start_row + i * dir_row, start_col + i * dir_col
        if not (0 <= r < rows and 0 <= c < cols) or gridname[r, c] != pattern1[i]:
            return False
    return True

directions=[(0,1),(0,-1),(1,0),(-1,0),
            (1,1),(-1,-1),(-1,1),(1,-1)]

def count_xmas(gridname):
    count=0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            for direction in directions:
                if check_direction(gridname,i,j,direction[0],direction[1]):
                    count+=1
    return count

print('part1:',count_xmas(grid))

def find_3x3_xmas(gridname, pattern):
    xmas_count = 0
    patterns=[np.rot90(pattern, k=i) for i in range(4)]

    for r in range(gridname.shape[0]-pattern.shape[0]+1):
        for c in range(gridname.shape[1]-pattern.shape[1]+1):
            subgrid=gridname[r:r+3,c:c+3]
            #compare to pattern
            for pattern_rotation in patterns:
                if compare_subgrid_to_pattern(subgrid,pattern_rotation):
                    xmas_count+=1
    return xmas_count

def compare_subgrid_to_pattern(subgrid,pattern):
    for r in range(subgrid.shape[0]):
        for c in range(subgrid.shape[1]):
            if pattern[r,c]!='.' and pattern[r,c]!=subgrid[r,c]:
                return False
    return True
print ('part2:',find_3x3_xmas(grid,pattern2))
