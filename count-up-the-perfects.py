"""
Karen really loves math. In particular, she loves the idea of having all numbers be described in a perfect manner. But, she needs your help to describe her list of numbers in the perfect fashion. Karen will give you some number N. In order to help her, you need to find the minimum number of perfect square numbers that add up to it. This way she can easily allocate the minimum correct amount of spaces for her given number to be perfect!

Input Format

N

Constraints

N > 0

Output Format

K, the number of perfect squares that add up to N

Sample Input 0

20
Sample Output 0

2
Explanation 0

16 
4 
20 = 16 + 4
"""

# SOLUTION

from sys import stdin
from math import sqrt

N = None
for line in stdin:
    N = int(line)

memo = [0, 1, 2, 3]

for i in range(4, N+1):
    memo.append(i)
    for j in range(1, i+1):
        temp = j*j
        if temp > i:
            break
        memo[i] = min(memo[i], memo[i-temp]+1)

print(memo[N])
