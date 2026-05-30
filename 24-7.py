"""
###Problem 7: Sort a list of alphanumeric strings based on product value of numeric character
in it. If in any string there is no numeric character take it’s product value as 1.
Input:
['1ac21', '23fg', '456', '098d','1','kls']
Output:
['456', '23fg', '1ac21', '1', 'kls', '098d']
"""
l=['1ac21', '23fg', '456', '098d','1','kls']
l1=[]
l2=[]
l3=[]
for i in l:
    p=1   
    for j in i:
        if j.isdigit():
            p=int(j)*p
    l1.append([p,i])
    l2.append(p)
#print(l1)        

#print(l2)
"""
l2=list(sorted(l2,reverse=True))
#print(l2)
for i in l2:
    for j in l1:
        if i==j[1]:
            if j[0] not in l3:
              l3.append(j[0])
print(l3)            
  """        
  # short curt
l2=list(sorted(l1,reverse=True))
l3=[i[1] for i in l2]
print(l3)
  