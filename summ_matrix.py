# 5 Numpy matrix.sum()

import numpy as np

a=np.matrix('[4,1; 12,3]')

sum=a.sum()
print(sum)



# import the important module in python 
import numpy as np 
			
# make matrix with numpy 
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]') 
print(gfg)
# applying matrix.sum() method 
geek = gfg.sum(axis = 1) 
geek1 = gfg.sum(axis = 0) 
print(geek) 
print(geek1) 
