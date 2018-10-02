"""
QUESTION

An ethics professor is sitting in a classroom, when all of a sudden crises strikes! The NSA has called to ask if certain students are present in the class. This professor has a list of students present in class, and decides to give it to you (The CA) instead. Check if any of the students are present in class today. (The NSA has really been slacking lately so they may look for the same student repeatedly).

EX:

Look for names here

This is the NSA

For these two lines of input you would print false because the word "This" does not appear in the sentence "Look for names here". Neither does "is" "the" or "NSA". Thus we print "false".

Input Format

The first line of input will contain space separated Strings that are the names of the students present. The second line of input will contain space separated strings that are the names of the students that the NSA is looking for.

Constraints

There will be no more than 1000 students in this class, and the NSA will look for no more than 100 of them.

Output Format

Print a true if the student is present, and false if the student is not.

Sample Input 0

This is a test case
look for names from the top.
Sample Output 0

false
"""

# SOLUTION

from sys import stdin

names = None
find = None

for line in stdin:
    if names:
        find = set(line.split(' '))
    else:
        names = set(line.split(' '))
        
for name in names:
    if name in find:
        print("true")
        exit()
    
print("false")
