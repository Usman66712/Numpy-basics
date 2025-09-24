import numpy as np

a=np.full((2,3),2)
print(a)
b=np.full((3,2),3)
print(b)

#MULTIPLICATION rule in linear algebra is that the coloum for firs tmatrix equals to coloumn of 2nd
mul=np.matmul(a,b)
print(mul)

c=np.array([[1,7,3],[4,9,6],[7,50,9]])
d=np.linalg.det(c)
print(d)

#so many linear stuff remaining learn all those, kaggle or what not 



#statisics 
min=np.min(c)
max=np.max(c)
print(min,max)
# you can also do axis and min on a certain row or coloumn 

print(np.sum(c))