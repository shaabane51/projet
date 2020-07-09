import numpy as np 
import matplotlib.pyplot as plt 

m = np.array([[0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 1, 0, 0, 0], [0, 1, 0, 0 ,0]]) 
cluster_1 = np.array([[1, 2, 3], [3, 4, 3]]) 


c = cluster_1   


for i in range(c.shape[1]): 
    for j in range(c.shape[1]): 
     if m[c[0,i]-1,c[1,j]-1]: 
      m[c[0,i]-1,c[1,j]-1] = 1

plt.matshow(m, cmap='jet', interpolation='nearest') 
plt.show()