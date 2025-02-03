#4 Select the elements from a given matrix

"""
With the help of Numpy matrix.take() method, 
we can select the elements from a given matrix 
by passing the parameter as index value of that element. 
It will return a matrix having one dimension

"""

import numpy as np

a=np.matrix('[4,1,12,3,4,7,8]')

select=a.take(2)

print(select)