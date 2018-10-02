"""
Reversing an integer is a classical problem. Now, let's make it a bit more challenging! Let's reverse an integer, add it to the 'unreversed integer' until all the digits in the new number are even!

Input Format

N Original Number

Constraints

0 < N < 1000000

Output Format

K where K is the new integer with all its digits even

Sample Input 0

41
Sample Output 0

242
Explanation 0

First reversed integer will be 14 
41 + 14 = 55 
55 + 55 = 110 
110 + 011 = 121 
121 + 121 = 242
"""

# SOLUTION

from sys import stdin

n = None
for line in stdin:
    n = line
    
def checkEven(n):
    return all(int(i) % 2 == 0 for i in n)

start = True
while not checkEven(n) or start:
    n = str(int(n) + int(n[::-1]))
    start = False
    
print(n)
