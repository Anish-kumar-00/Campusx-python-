"""
0.0.2 Problem 9: Convert Character Matrix to single String using string comprehen-
sion.
Example 1:
Input:
[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
Output:
campux is best channel
"""

l=[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
l1=[]
for i in l:
    s=''
    for j in i:
        s=s+j
    print(s)
#print(l1)    