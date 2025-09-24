import numpy as np

a=np.identity(3)
print(a)

#repeating an array 
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)

# a bit complex matrix 

output=np.zeros((5,5))

g=np.ones((3,3))
g[1,1]=9
output[1:4,1:4]=g
print(output)

 #be careful of copying please
# lets say 
b=np.array([1,2,3])
c=b
print(c)
#but here is the issues like, same as c++
c[0]=10022
print(c)
print(b)
#see the b change cause pointer is pass by address 

# here is the solution
b=np.array([1,2,3])
c=b.copy()
c[0]=10022
print(b)


