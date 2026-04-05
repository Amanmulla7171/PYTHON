import numpy as np

arr=np.array([10,20,30,40,50,6])
#print(arr[[0,2,4]])
#print(arr[[arr>25]])
#reshape-its not make copy its create the view by in matrix
reshaped_arr=arr.reshape(2,3)
print(reshaped_arr) 
print("-----------------------")

#flattering array
#.ravel-return the view
#.flatten()-return the copy
arr2d=np.array([ [10,20,30], [40,50,6]])
print(arr2d.flatten())
print(arr2d.ravel())



