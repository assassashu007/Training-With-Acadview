print("Q.1- Create a list with user defined inputs.")

our_list = []


print("Enter no of elements in a list")
x = int(input())
print("Enter %d list values" % (x))

for i in range(0, x):
    our_list.append(input())

print(our_list)






print("Q.2- Add the following list to above created list:[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]")

our_list.append('google')
our_list.append('apple')
our_list.append('facebook')
our_list.append('microsoft')
our_list.append('tesla')

print(our_list)





print("Q.3- Count the number of time an object occurs in a list. ")

print("Google occurs : " + str(our_list.count('google')))
print("Apple occurs : " + str(our_list.count('apple')))
print("Facebook occurs : " + str(our_list.count('facebook')))
print("Microsoft occurs : " + str(our_list.count('microsoft')))
print("Tesla occurs : " + str(our_list.count('tesla')))





print("Q.4- create a list with numbers and sort it in ascending order.")

our_list2 = []

print("Enter no of elements :")
y = int(input())

print("Enter %d elements" %(y))

for i in range(0, y):
    our_list2.append(int(input()))

print(our_list2)

our_list2.sort()
print("Sorted list : ")
print(our_list2)




print("Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]")

arr_a = [1,10,19,21]
arr_b = [6,8,11,30]
arr_c = []
print("Array A : " + str(arr_a))
print("Array B : " + str(arr_b))

print("Merging of array A and array B into array C")
arr_c = arr_a + arr_b
print(arr_c)

print("Sorting of Array C")
arr_c.sort()
print(arr_c)






print("Q.6-Implement a stack and queue using lists.")

print("\nImplementing Stack :")
stack = ["Ashu", "is", "a"]
stack.append("good")
stack.append("boy")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)


print("\n\nImplementing Queue :")
from collections import deque
queue = deque(["Ashu", "is", "good", "boy"])
print(queue)
queue.append("thank")
print(queue)
queue.append("you")
print(queue)
print(queue.popleft())                 
print(queue.popleft())                 
print(queue)




print("Q.7- Count even and odd numbers in that list.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
