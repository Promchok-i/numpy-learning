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


# Reshape & Resize : Resize will change array permanently
arr1.reshape([5,1])
arr1.resize([5,1])

# Flatten and Ravel : change to 1D, Ravel = if r[x] changes, arr2[x] changes too.
arr2.flatten()
r = arr2.ravel()

# Transpose switch row and column
arr2.transpose()

# Statistics
arr1.sum()
arr1.prod()
arr1.mean()
arr1.min()
arr1.max()
arr1.argmax() # index at max
arr1.argmin() # index at min
np.max(arr2, axis=1) # 2D : max of each row, axis=0 : each column

# Dot product : rows and columns of both arrays must equal (Ex. [2,2] and [2,2] : a.dot(b))

# Concatenate, Append, Insert (np.concatenate((a,b)), np.append(a, 100))
np.append(arr2,[[10,20,30]], axis=0)
np.insert(arr1,(1,3),100)
np.insert(arr2,1,[33,44,55],axis=1)

# Delete, Split
np.delete(arr1,2)
np.delete(arr2,2,axis=0)
np.hsplit(arr1,3) # Seperate to new arrays in horizontally | | |
np.vsplit(arr2,3) # Seperate to new arrays in vertically -- __