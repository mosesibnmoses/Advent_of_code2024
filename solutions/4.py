import re

import numpy as np
from pycparser.c_ast import Return

from utils.helpers import read_grid


filename= "../data/4_input.txt"
grid=read_grid(filename)
pattern = 'XMAS'
rows, cols = grid.shape

def check_direction(grid,start_row,start_col,dir_row,dir_col):
    for i in range(len(pattern)):
        r, c = start_row + i * dir_row, start_col + i * dir_col
        #print (r,c)
        if not (0 <= r < rows and 0 <= c < cols) or grid[r, c] != pattern[i]:
            return False
    return True

directions=[(0,1),(0,-1),(1,0),(-1,0),
            (1,1),(-1,-1),(-1,1),(1,-1)]

def count_xmax(gridname):
    count=0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            for dir in directions:
                if check_direction(gridname,i,j,dir[0],dir[1]):
                    count+=1
    return count

print(count_xmax(grid))