# 6  Calculate the sum of the diagonal elements of a NumPy array\\

#Method 1: Finding the sum of diagonal elements using numpy.trace()

import numpy as np

array = np.array([[55, 25, 15], 
                    [30, 44, 2], 
                    [11, 45, 77]]) 


print("original array")
print(array)

diagonal_sum=array.trace()
print("diagonal sum is s:-")
print(diagonal_sum)