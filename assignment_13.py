print("Q.1- Write a Python program to read last n lines of a file\n")


n = int(input("Enter the line from where you want to read : "))
n = n-1
file = "test.txt"
with open(file,'r') as f :
    a = f.readlines()

    while n<len(a) :
        print(a[n])
        n=n+1









print("\n\nQ.2- Write a Python program to count the frequency of words in a file.\n")


from collections import Counter

def word_count(file):
        with open(file) as f:
                return Counter(f.read().split())

print("Number of words in the file with their frequency : \n",word_count("test.txt"))









print("\n\nQ.3- Write a Python program to copy the contents of a file to another file.\n")


with open("test.txt", "r") as f:
    with open("OUTPUT.txt", "w") as f1:
        for word in f:
            f1.write(word)

print("New copied file created is OUTPUT.txt")









print("\n\nQ.4- Write a Python program to combine each line from first file with the corresponding line in second file.\n")


with open("test.txt", "r") as f:
    a = f.readlines()

with open("OUTPUT.txt", "r") as f:
    b = f.readlines()

i=0
while i<len(a):
    print("From text.txt   :" + a[i] + "\n" + "from OUTPUT.txt :" +b[i])
    i+=1










print("\n\nQ.5- Write a Python program to write 10 random numbers into a file.")
print("     Read the file and then sort the numbers and then store it to another file.\n")


import random

b=[]
with open("test2.txt", "w") as f:
    for i in range(10):
        a =random.random()
        b.append(a)
        f.write(str(a) + "\n")

a = b.sort()

with open("OUTPUT2.txt", "w") as f:
    for i in range(len(b)):
        f.write(str(b[i]) + "\n")



