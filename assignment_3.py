print("Q.1- Write a program to create a tuple with different data types and do the following operations.")
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print("Tuple : " + str(tuple1))

print("\n\nQ.Find the length of tuples")
print("Length of tuple : "+str(len(tuple1)))




print("\n\nQ.2-Find largest and smallest elements of a tuples.")

print("Largest element is : " + str(max(tuple1)))
print("Smallest element is : " + str(min(tuple1)))




print("\n\nQ.3- Write a program to find the product of all elements of a tuple. ")

lis = list(tuple1)       #changing the tuple into list to make calculation easy !
prod = 1
for i in range(0, 6):
	prod = prod * int(lis[i])
print(str(prod))




print("\n\nQ.1- Create two set using user defined values. ")


a = set()
b = set()
print("Enter the length of set a : ")
n = int(input())
for i in range(0, n):
        print("Enter value : ")
        a.add(input())
print("Enter the length of set b : ")
m = int(input())
for i in range(0, m):
        print("Enter value :")
        b.add(input())
print("\nSet A : " + str(a))
print("\nSet B : " + str(b))


print("\n\n1. Calculate difference between two sets.")
diff1 = a - b
diff2 = b - a
print("Difference of a-b is : ")
print(diff1)
print("Difference of b-a is : ")
print(diff2)



print("\n\n2. Compare two sets.")
len1 = int(len(a))
len2 = int(len(b))
if len1 == len2:
        print("Set A and B are of same length")
if len1 > len2:
        print("Set A is bigger")
if len1 < len2:
        print("Set B is bigger")



print("\n\n3. Print the result of intersection of two sets.")
print(a & b)




print("\n\nCreate a dictionary to store name and marks of 10 students by user input.")

dictionary = {}

count = 0

while count < 10:
   name = input("Enter your name: ")
   mark = input("Enter your mark out of 100: ")
   if name not in dictionary:
       dictionary[name] = mark
       count = count + 1
   else:
       name = input("Enter a unique name: ")
       mark = input("Enter the mark out of 100: ")
       if name not in dictionary:
          dictionary[name] = mark
          count = count + 1

print(dictionary)



print("\n\nQ.2-Sort the dictionary created in previous question according to marks. ")

print(sorted(dictionary))




print("\n\nQ.3- Count the number of occurrence of each letter in word 'MISSISSIPPI'. Store count of every letter with the letter in a dictionary.")

a = ['M','I','S','S','I','S','S','I','P','P','I']
print(a)
print("Occuranace of Each Alphabet is :")
print("Letter M : " + str(a.count('M')))
print("Letter I : " + str(a.count('I')))
print("Letter S : " + str(a.count('S')))
print("Letter P : " + str(a.count('P')))

dictionary = {"M":a.count('M'),"I":a.count('I'),"S":a.count('S'),"P":a.count('P')}
print("\nOutput in dictionary is :" + str(dictionary))
