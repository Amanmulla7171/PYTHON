import numpy as np

#np.concatenate((arrar1,array2),axis=0)
#axis 0-rowwise
#axis 1-vertically

arr1=np.array([1,2,3])
arr2=np.array([4,5,6,7])
new_arr=np.concatenate((arr1,arr2))
print(new_arr)