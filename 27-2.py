"""
###Q2: Multiply Adjacent elements (both side) and take sum of right and lest side multiplication
result.
For eg.
The original tuple : (1, 5, 7, 8, 10)
Resultant tuple after multiplication :
(1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)
output-(5, 40, 91, 136, 80)

"""
l1=list(1, 5, 7, 8, 10)

l2=[]
for i in l1:
    k=l1.index(i)
    if k>0 and k<(len(l1)-1):
       l2.append(i*(l1[k-1]+l1[k+1]))
    elif k==0:
       l2.append(i*(l1[k+1]))
    else:
        l2.append(i*(l1[k-1]))
print(l2)        