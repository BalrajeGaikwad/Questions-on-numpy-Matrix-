# 3 Find the number of rows and columns of a given matrix using NumPy

"""
We can find matrix dimension with three ways:

1 Using shape Attribute
2 Using Indexing
3 Using numpy.reshape()

"""
#Way 1: Using .shape Attribute

import numpy as np

arr=np.array([[1,2,3,4],[5,6,7,8]])

dimensions=arr.shape
rows, columns=dimensions

print("rows :-",rows)
print("columns :-",columns)

#Way 2: Using Indexing

import numpy as np

matrix=np.array([[1,2,3,4],[5,6,7,8]])
rows=matrix.shape[0]
columns=matrix.shape[1]

print("rows using indexing :-",rows)
print("columns usinf indexing :-",columns)

#Way 3: Using numpy.reshape()

import numpy as np

matrix=np.arange(1,10).reshape((3,3))

print(matrix)

print(matrix.shape)
