
"""
###Q1: Join Tuples if similar initial element While working with Python tuples, we can have a
problem in which we need to perform concatenation of records from the similarity of initial element.
This problem can have applications in data domains such as Data Science.
For eg.
Input : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
Output : [(5, 6, 7, 8), (6, 10), (7, 13)]
"""


l= [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
l1=[]
for i in l:
    temp=[i[0]]
    for j in l:
        if i[0]==j[0]:
           temp.append(j[1])
    if(tuple(temp) not in l1):       
     l1.append(tuple(temp))  
    temp=[]
print(l1)    