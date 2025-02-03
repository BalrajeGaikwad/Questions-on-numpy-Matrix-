#  Adding and Subtracting Matrices in Python

import numpy as np

a=np.array([[1,2],[3,4]])
b=np.array([[4,5],[6,7]])

print("Array A")
print(a)

print("Array B")
print(b)

print("Addition of A AND B")
print(np.add(a,b))

print("Subtraction of A And B")
print(np.subtract(a,b))


# METHOD 3:Using nested loops
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]

print("print the elements of first matrix ")

for row in matrix1:
    for element in row:
        print(element, end=" ")

    print()

print("length of matrixq :-",len(matrix1))
print("print the element of second matrix ")

for row in  matrix2:
    for element in matrix2:
        print(element, end=" ")

    print()

result=[[0,0],[0,0]]
#subtracting two matrix
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]=matrix1[i][j]- matrix2[i][j]

#printing the result 
print("Subtration of two matrix ")

for row in result:
    for element in row:
        print(element, end=" ")

    print()