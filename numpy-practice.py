import numpy as np

# array 1,2,3 D
arr1 = np.array([1,2,3,4,5])
arr1[3] = 99
print(arr1, arr1.ndim, arr1[2])
#[ 1  2  3 99  5] 1 3

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2[1][2] = 99
print(arr2, arr2.ndim, arr2[2][1])
"""[[ 1  2  3]
 [ 4  5 99]
 [ 7  8  9]] 2 8"""

arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr3[1][0][1] = 99
print(arr3, arr3.ndim, arr3[1][1][2])
"""[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7 99  9]
  [10 11 12]]] 3 12"""

# check data type for each Array
print(arr3.dtype)

# Matrix : 0, 1, full, empty, Identity 
np.zeros([3,3])
np.ones([2,2], dtype="int")
np.full([3,3], 7)
np.empty([3,4])
np.identity(3, dtype="int")
np.eye(3,4,k=2) # k : move No.1

# Linspace, Arange : No.2 in Linspace = length, No.2 in arange = steps
np.linspace(1,10,2,endpoint=False) # endpoint = False : Not include endpoint
np.arange(1,10,2)

# Random
np.random.random([3,3])

# Attributes
arr2.ndim 
arr2.dtype
arr2.shape # (3,3)
arr2.size # show 9 items
arr2.itemsize #show in bytes

# Slice
arr1[1:5:2] #1D
arr2[1:2,1:2] #2D

# Index Operator
arr1[[1,4]]
arr2[arr2<5]**2

# +,-,*,/,//,% : shape must be equal or broadcasting