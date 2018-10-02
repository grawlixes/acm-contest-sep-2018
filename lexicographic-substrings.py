"""
Given a string, find the lexicographic first and last sub-strings of the input string where the first character is a vowel and the last character is a consonant. A substring is a continuous sequence of characters that occurs in the string

Lexicographic ordering means the same ordering that would be used in a dictionary. For example:

ab > a

st > se > eg

Input Format

S, the input string

Constraints

length of S will be >= 3

Output Format

Substring1, The lexicographically first string satisfying the requirements

Substring2, The lexicographically last string satisfying the requirements

Sample Input 0

aba
Sample Output 0

ab
ab
Sample Input 1

iloveacm
Sample Output 1

ac
oveacm
"""

# SOLUTION

from sys import stdin

s = None
for line in stdin:
    s = line
    
vowels = ['a', 'e', 'i', 'o', 'u']    
# smallest
smallest = None
largest = None
for i in range(len(s)):
    if s[i].lower() in vowels and (not smallest or s[i] >= largest[0] or s[i] <= smallest[0]):
        for j in range(i+1, len(s)):
            if s[j].lower() not in vowels:
                cur = s[i:j+1]
                if not smallest or smallest > cur:
                    smallest = cur
                if not largest or largest < cur:
                    largest = cur
                    
print(smallest)
print(largest)
