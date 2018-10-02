"""
Jordan hates spiders. If he ever sees one in his room he immediately wants to move as far away from the spider as he can. The goal is to find the spot in the room that Jordan wants to move to, which is the location where the spider will have to take the most steps in order to reach him. The room is represented as a grid, with 'o' representing space to move, and 'x' representing obstacles.

Input Format

Srow, Scol, row and column coordinates of the spider (oriented so that 0,0 means top left)

Jrow, Jcol, row and column coordinates of Jordan (oriented so that 0,0 means top left)

N, number of rows and columns in the map of the room

N by N grid with 'o' representing space to move, and 'x' representing obstacles

Constraints

4 < N < 50

All coordinates are within the grid

The spider will not have the same coordinates as Jordan

No spaces will be completely blocked off from the rest of the grid

You may assume there will be only one location that is farthest from the spider

Output Format

JrowFinal, JcolFinal, The coordinates that Jordan wants to get to to escape the spider

Sample Input 0

2,1
3,4
5
ooooo
ooooo
ooxoo
ooxoo
ooooo
Sample Output 0

3,4
Sample Input 1

3,1
2,4
5
xxoxo
ooooo
xxxoo
ooxoo
xoooo
Sample Output 1

1,0
"""

# SOLUTION

from sys import stdin

spider = None
N = None
grid = []
one = 0
for line in stdin:
    if not spider:
        spider = (int(line[:line.find(',')]), int(line[line.find(',')+1:]))
    elif spider and one < 2:
        one += 1
    elif one == 2:
        grid.append(line.strip())
        
from queue import Queue
Q = Queue()
# BFS
# (i, j, distance)
Q.put((spider[0], spider[1], 0))

ret = (-1, -1)
retDist = -1
visited = set()
while Q.qsize():
    cur = Q.get()
    i = cur[0]
    j = cur[1]
    dist = cur[2]
    
    visited.add((i, j))
    
    if retDist == -1 or dist > retDist:
        retDist = dist
        ret = (i, j)
    
    if i != len(grid)-1 and grid[i+1][j] != 'x' and ((i+1, j) not in visited):
        Q.put((i+1, j, dist+1))
    if j != len(grid[i])-1 and grid[i][j+1] != 'x' and ((i, j+1) not in visited):
        Q.put((i, j+1, dist+1))
    if i != 0 and grid[i-1][j] != 'x' and ((i-1, j) not in visited):
        Q.put((i-1, j, dist+1))
    if j != 0 and grid[i][j-1] != 'x' and ((i, j-1) not in visited):
        Q.put((i, j-1, dist+1))
        
print(str(ret[0]) + ',' + str(ret[1]))
