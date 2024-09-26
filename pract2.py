from numpy.linalg import inv
import numpy as np
arr1 = np.array([11,2,3,40,5,6])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# print(np.zeros((2,3)))
# print(np.ones((2,3)))
# print(np.empty((2,3)))
# print(np.arange(0,10,2))
# print(np.linspace(0,10,5))
# print(np.random.randint((2,3)))
# print(arr2.shape)
# print(arr3.ndim)
# print(arr3.dtype)
# print(arr3.size)
# print(arr3.itemsize)
# print(arr3.nbytes)
# print(arr3[0,1,2])
# print(arr3)
# print(arr3[1,1,1])

# print(arr1[0])
# print(arr1[0:3])
# print(arr1[:3])

# print(arr1[-1])
# print(arr1[-3:])
# print(arr1[:-3])

# print(arr2)
# print(arr2[0,1])
# print(arr2[:,1])
# print(arr2[1,:])
# print(arr2[1,1:])
# print(arr2[0,:])
# print(arr2[:,0])

# print(arr1 * 2)

# print(arr2)
# print(np.sum(arr2))
# print(np.sum(arr2, axis=0))
# print(np.mean(arr2))
# print(np.mean(arr2, axis=0))
# print(np.min(arr2))
# print(np.min(arr2, axis=0))
# print(np.max(arr2))
# print(np.std(arr2))

# print(arr1.reshape(2,3))
# print(arr1.reshape(3,2))
# print(arr1.reshape(6,1))
# print(arr1.reshape(1,6))
# print(arr1.reshape(6))
# print(arr1.reshape(6,1).shape)
# print(arr1.reshape(6,1).ndim)
# print(arr1.reshape(6,1).dtype)
# print(arr1.reshape(6,1).size)
# print(arr1.reshape(6,1).itemsize)
# print(arr1.reshape(6,1).nbytes)
# print(arr1.reshape(6,1)[0])
# print(arr1.reshape(6,1)[0:3])
# print(arr1.reshape(6,1)[:3])
# print(arr1.reshape(6,1)[-1])
# print(arr1.reshape(2,3).T)
arr5 = np.array([[1,2],[3,4]])
# arr4 = np.array([10,20])
# result = arr5 + arr4
# print(result)
# print(arr5.ndim)
# print(arr5.shape)

# print(np.dot(arr2,arr2.T))

# print(np.matmul(arr2,arr2.T))

# print(np.linalg.det(arr5))
# print(arr5)
# print(inv(arr5))


# arr6 = np.random.randint(0,10,(3,3))
# print(arr6)

# arr7 = np.random.random((2,2))
# print(arr7)

# print(np.sort(arr1))

# print(np.unique(arr1))
# print(np.concatenate((arr2,arr2),axis=0))
# print(np.concatenate((arr2,arr2),axis=1))

# print(np.vstack((arr2,arr2)))
# print(np.hstack((arr2,arr2)))

# np.save('arr1.npy',arr1)
# arr8 = np.load('arr1.npy')
# print(arr8)

# arr9 = np.random.randint(0,10,(6,6))
# print(arr9)
# print(arr9[1::2,::2])
# sorted_by_second_row = arr9[:,arr9[1,:].argsort()]
# sorted_by_second_column = arr9[arr9[:,1].argsort()]
# print(arr9)
# print(sorted_by_second_row)
# print(sorted_by_second_column)
# print(arr1)
# print(np.where(arr1>3))

print(np.where(arr1>3,1,0))
print(np.where(arr1>3,1,arr1))
print(np.where(arr1>3,arr1,0))
print(np.where(arr1>3,arr1,10))
