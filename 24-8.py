"""
Problem 8: Split String of list on K character.
Example :
Input:
['CampusX is a channel', 'for data-science', 'aspirants.']
Output:
['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']

"""

l=['CampusX is a channel', 'for data-science', 'aspirants.']
l1=[]
for i in l :
     s=''
     for j in i:
         if j!=' ':
             s=s+j
         else :   
             l1.append(s)
             s=''
     l1.append(s)
print(l1)

""""
l = ['CampusX is a channel', 'for data-science', 'aspirants.']

l1 = []

for i in l:
    s = ''

    for j in i:
        if j != ' ':
            s += j
        else:
            l1.append(s)
            s = ''

    if s:
        l1.append(s)

print(l1)
"""