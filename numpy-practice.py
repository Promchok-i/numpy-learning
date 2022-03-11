import numpy as np

# array 1,2,3 D
arr1 = np.array([1,2,3,4,5])
arr1[3] = 99
print(arr1, arr1.ndim, arr1[2])

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2[1][2] = 99
print(arr2, arr2.ndim, arr2[2][1])

arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr3[1][0][1] = 99
print(arr3, arr3.ndim, arr3[1][1][2])
