import numpy as np
from numpy.matlib import identity

hours=np.arange(0,22,3)
line=np.linspace(0,1,5)
zeros=np.zeros(6,dtype=int)
unknown_table=np.full((2,3),-1)
identity=np.eye(3)
print('1oe')
print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)

print('2oe')
print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])


temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print('3oe')
print("\n",temperatures.shape)
print("\n",temperatures.ndim)
print("\n",temperatures.size)
print("\n",temperatures[1,3])
print("\n",temperatures[0,:])
print("\n",temperatures[:,-1])
print("\n",temperatures[0:2,1:])
print("\n",temperatures[0:2,1:3])

print('4oe')
matrix = np.arange(1, 26).reshape(5, 5)
print("\n",matrix[0:3,:])
print("\n",matrix[-2:,:])
print("\n",matrix[:,:2])
print("\n",matrix[-2:,-2:])
print("\n",matrix[-2:,-2:])
print("\n",matrix[0:3,:].shape)
print("\n",matrix[-2:,:].shape)
print("\n",matrix[:,:2].shape)
print("\n",matrix[-2:,-2:].shape)
print("\n",matrix[-2:,-2:].shape)

print("\n",'5oe')
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
changed_hours = hours.copy()
changed_hours[2:5]=99
changed_hours[::2]=-1
print("\n",hours)
print("\n",changed_hours)
# без copy мы бы работали с hours

changed_matrix = matrix.copy()
changed_matrix[1,:]=0
changed_matrix[:,-1]=-1
changed_matrix[1:-1,1:-1]=100
print("\n",changed_matrix)

print("\n",'6oe')
numbers=np.arange(0,12)
table=numbers.reshape(3,4)
transposed=table.T
print("\n",numbers)
print("\n",table)
print("\n",transposed)


