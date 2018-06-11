print("Q.1- Take 10 integers from user and print it on screen.")


a=[0]*10

#to take 10 inputs from user and assigning it to list a using while loop
i=0
while i < 10:
    a[i] = int(input("Enter value " + str(i+1) +" : "))
    i+=1


#to print the values entered by user using while loop
i=0
while i<10:
    print(a[i])
    i+=1









print("\n\nQ.2- Write an infinite loop.An infinite loop never ends. Condition is always true. ")


while True:
    print('Infinity loop..... PLEASE ENTER   " Ctrl + C " TO EXIT')









print("\n\nQ.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.")

n = int(input("Enter number of elements to be inputed : "))
a = [0]*n
b = [0]*n

i=0
while i < n:
    a[i] = int(input("Enter elements : "))
    i+=1

j=0
while j < n:
    b[j] = a[j] * a[j]
    j+=1

print("Squares of elemnts is :")
k=0
while k < n:
    print(str(b[k]))
    k+=1








print("\n\nQ.4- From a list containing ints, strings and floats, make three lists to store them separately ")


a = [10, 'Ashutosh', 11.23, 'Rawat', 20, 41.667, 30]
str_list = []
float_list = []
int_list = []
print("\nORIGINAL LIST IS : " + str(a))


i=0
while i < len(a):
    if type(a[i]) == str:
        str_list.append(a[i])
    if type(a[i]) == float:
        float_list.append(a[i])
    if type(a[i]) == int:
        int_list.append(a[i])
    i+=1

print("\nString List is : " + str(str_list))
print("Float List is : " + str(float_list))
print("Integer List is : " +str(int_list))





print("\n\nQ.5- Using range(1,101), make a list containing even and odd numbers. ")


new_list = []
odd = []
even = []
x = range(1,101)

new_list = list(x)

i=1
while i < len(new_list):
    if i%2 == 0:
        odd.append(new_list[i])
    else:
        even.append(new_list[i])
    i+=1


print("\nODD numbers are : " + str(odd) + "\n")
print("EVEN numbers are :" + str(even))




print("\n\nQ.6- Print the following patterns:")
print("*")
print("**")
print("***")
print("****")



for x in range(1,5):
    for y in range(1,x-4):
        print("*")







print("\n\nQ.7- Create a user defined dictionary and get keys corresponding to the value using for loop.")


dic = {'a': 101, 'b': 102, 'c': 103, 'd': 104, 'e': 105, 'f': 106, 'g': 107}
print("\nOriginal Dictionary is :")
print(str(dic) + "\n")
dic_keys = list(dic.keys())
dic_values = list(dic.values())

for x in range(0,len(dic)):
    print(str(dic_keys[x]) + ": " + str(dic_values[x]) + "\n")







print("Q.8- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.")

n = int(input("\nEnter number of elements to to entered in a list : "))
a = []
count = 0
delete = []


for i in range(0,n):
    a.append(int(input("Enter a integer value :")))


print("\nList is :" + str(a))
s = int(input("Enter the value to be searched and deleted : "))

for i in range(0,n):
    if a[i] == s:
        delete.append(int(i))
    else:
        continue

print(str(s) + " is present in indexe(s) : " + str(delete))
for i in range(0,len(delete)):
    a.remove(s)


print("\nAfter iteration List is : " + str(a))