#missing value 3 function
#np.isnan-detect missing value
#np.nan_to_num()-replace by other number to tht number
#np.isinf()-to detect infinite value
import numpy as np
#detect-
arr=np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))

#replace-
replaced_arr=np.nan_to_num(arr,nan=100)
print(replaced_arr)

#infinite value-its have positive or negative infinite
infinite=np.array([1,2,np.inf,4,np.nan,6])
print(np.isinf(infinite))