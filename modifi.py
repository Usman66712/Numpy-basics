import numpy as np

before=np.array([[1,2,3],[4,5,6]])
print(before)
after=before.reshape((6,1))
print(after)


#stacking one array on the toip of another 

a=np.array([[1,2,3]])
b=np.array([[7,8,9]])
stack=np.vstack([a,b])
print(stack)

h1=np.ones((2,4))
h2=np.zeros((2,2))
print(np.hstack((h1,h2)))
