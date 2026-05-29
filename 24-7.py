"""
0.0.7 Problem 14: Write a list comprehension that can transpose a given matrix
matrix = [ [1,2,3], [4,5,6], [7,8,9]]
[1, 4, 7] [2, 5, 8] [3, 6, 9]
"""
matrix = [ [1,2,3], [4,5,6], [7,8,9]]
x=[]
for i in range (0,3,):
     temp=[]
     for l in range(0,3,):
         temp.append(matrix[l][i])
     x.append(temp)
print(x)     