import numpy as np
from random import *

print("Q1. Create a numpy array with 10 elements using np.random and find mean of the elements using basic numpy functions.\n")

arr1 = np.random.random((10,1))
print("Mean: ",np.average(arr1))





print("\n\nQ2. Create a numpy array with 20 elements using np.random find the variance & standard deviation.\n")

arr2 = np.random.random((20,1))
print("Variance: ",np.var(arr2))
print("Standard Deviation: ",np.std(arr2))



print("\n\nQ3. Creatae two nuumpy arrays & find their matrix multiplication & hence the sum of elements of new array.\n")

a = np.random.random((10,20))
b = np.random.random((20,25))
c=np.dot(a,b)
print("First array: \n", a)
print("Second array: \n", b)
print("New Array: n", c)
print("Shape of new matrix: ",np.shape(c))
print("Sum of elements of new array: ",np.sum(c))



print("\n\nQ4. Apply the formula: 1/(1+np.exp(-arr3)) on each element of a previously generated array to print a new array using numpy.\n")

arr3 = np.random.random((10,1))
print("\nOld array: \n", arr3)
func = 1/(1+np.exp(-arr3))
print("New array: \n",func)