import numpy as np
a=np.array([[1,2,3,4,5,6,7],[20,30,40,50,60,70,80]])
print(a)
#GET A SPECIFIC INDEX FROM ARRAY 2D(R,C)
print(a[1,5])
#you can also use negative notation, eg list start from 0 to 6 each row so i will say in reverse starts from-1
print(a[1,-1])
#to get a specifuic row you need to select row 0 indexed and then : which means slicing upto the length of row
print (a[0,:])
#to get a specifuic coloum you need to slice the first row as its (r,c)and then  you need to select coloum 0 indexed 9remember slicing will give both row for specific row you need to type row number 
print(a[:,3])
#if we want to get specific elements between two points eg in row 0, startindex is 3 endindex is 7 and we want the elements in btw
print(a[0,1:6]) # that means 0 row anbd give elements in between 1 and 6

print(a[0,1:6:2])# that means 0 row anbd give elements in between 1 and 6 and i we want to jump in a specfic number and the number number after comma 
#IF YOU WANT TO CHANGE AN ELEMENT easy way its its (row coloum) so 
a[1,4]=65
print(a[1])
#if you want to do it for both rows just do like before 
a[:,3]=55#:get both rows and 3 is the 3rd indexx (0 indexing) for both rows 
print(a)
#or you can give multiple numbers in sequence a[:,3]=[55,56]

