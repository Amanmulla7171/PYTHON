import numpy as np

#broadcasting is numpy way where simple array type perform the calculation without loop
vector=np.array([100,200,300])
"""
result=arr*2
print(result)
result=arr+10
print(result)
"""
#1D and 2D array
matrix=np.array([[1,2,3],[4,5,6]])
result=matrix+vector
print(result)
