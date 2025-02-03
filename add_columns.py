# Add columns in the Numpy array

import numpy as np

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("original array")
print(str(arr))

column_to_be_added=np.array([[9],[8],[7]])

new=np.append(arr, column_to_be_added, axis=1)
print("new")
print(new)