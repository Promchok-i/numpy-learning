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

