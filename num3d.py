#lets go for a 3d array, so it goes like axis which is 3 for 3d and 2 for 2d , then rows and coloum as before
import numpy as np
a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# so axis is 3 
print(a[:,1,:])
#so its printing first row in all of access the axis three lets try different operation
print(a[1,1,1])
#initializing  different types of arrays 
b=np.zeros((2,2,2),dtype='int32')
print(b)
#next is all 1ss matrix  np.ones like last one and you can specify data types, 
#for any other number it will be, n.full and it takes  2 parameters 
c=np.full((3,1),99)

print(c)
#you can also pass the shape of another array you built and then give the number you want init np.full_like

d=np.full_like((a),9)
print(d)
#print random numbers 
e=np.random.rand(4,2)
print(e)
f=np.random.randint(21,33,size=(3,3)) #33 is max value  and if you want min to max you can 0,33
print(f)