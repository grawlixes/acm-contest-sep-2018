"""
you've been trapped in merlin's maze and there's only one way out! Well, actually that's not really true, because merlin have devised a maze like no other. Instead of a typical maze where you have to find the exit, merin's maze has an exit which will teleport randomly, sometimes not even appearing at all! or appearing in several places at once! Luckilly, you've been given a map of the maze, which marks where the exit can be and when it will be there, can you figure out the eariest you can escape the maze?

Input Format

You're given two numbers R and N where R is the number of "rounds" in the maze (aka when the exit locations reset) and N in the dimensions of the board (so N=3 is a 3x3 board)

The next input is N lines, each one N symbols long, which is the maze.

The maze is made up of a few symbols,

o - free space

x - wall

s - start location

0-9 - exit locations

the way the exits work is the maze is on a timer, every move increases the timer by 1, but you can also wait for time to pass. The exit locations are only valid if you're at that step in the current round.

Constraints

R <= 10 N <= 20

Output Format

output a single number, the soonest you can exit the maze.

Sample Input 0

1 3
soo
ooo
oo0
Sample Output 0

4
Sample Input 1

4 3
s32
ooo
ooo
Sample Output 1

2
Sample Input 2

4 3
so1
ooo
ooo
Sample Output 2

5
"""

# SOLUTION

from sys import stdin

R = None
grid = []
for line in stdin:
    if not R:
        R = int(line[:line.find(' ')])
    else:
        grid.append(line.strip())

from queue import Queue
Q = Queue()
# BFS
# (i, j, cur, tot)
ret = float('inf')
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 's':
            Q.put((i, j, 0, 0))

visited = {}
while Q.qsize():
    cur = Q.get()
    i = cur[0]
    j = cur[1]
    cur_R = cur[2]
    total = cur[3]
    
    visited[(i, j)] = total
    
    if grid[i][j].isdigit():
        add = int(grid[i][j]) - cur_R
        if cur_R > int(grid[i][j]):
            add = (R - cur_R) + int(grid[i][j])
        ret = min(ret, total + add)
        
    if i != len(grid)-1 and grid[i+1][j] != 'x' and ((i+1, j) not in visited or visited[(i+1, j)] >= total+1):
        Q.put((i+1, j, max(((cur_R+1)%(R+1)), 1), total+1))
    if j != len(grid[i])-1 and grid[i][j+1] != 'x' and ((i, j+1) not in visited or visited[(i, j+1)] >= total+1):
        Q.put((i, j+1, max(((cur_R+1)%(R+1)), 1), total+1))
    if i != 0 and grid[i-1][j] != 'x' and ((i-1, j) not in visited or visited[(i-1, j)] >= total+1):
        Q.put((i-1, j, max(((cur_R+1)%(R+1)), 1), total+1))
    if j != 0 and grid[i][j-1] != 'x' and ((i, j-1) not in visited or visited[(i, j-1)] >= total+1):
        Q.put((i, j-1, max(((cur_R+1)%(R+1)), 1), total+1))
        
print(ret)
