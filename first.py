import numpy as np 
a=np.array([1,2,3], dtype='int16')
print(a)
b=np.array([[7.0,8.0,9.0],[10.0,11.0,12.0]])
print(b)
c=a*b
print(c)
print(a.ndim)
print(b.ndim)
print(b.shape)
print(a.dtype)
a.itemsize
a.nbytes