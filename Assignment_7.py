print("Q.1- What is Time Tuple?\n\n")

import time

a = time.ctime()     # here a stores a string formated time eg: 'Wed Jun 13 23:03:47 2018'
print("time.ctime() returns a STRING.\n")
print("Example : " + a +"\n")


b = time.strptime(a)
print("time.strptime(string) returns a TIME TUPLE\n")
print("Example : " + str(b))






print("\n\nQ.2- Write a program to get formatted time.\n")


import time

print("Formatted current time is : " + time.asctime())





print("\n\nQ.3- Extract month from the time.\n")

import time

print("\nCurrent Time is : " + time.ctime() + "\n")
a = list(time.ctime())
print("Extracted current month is : " + a[4] + a[5] + a[6])






print("\n\nQ.4- Extract day from the time.\n")

import time

print("\nCurrent Time is : " + time.ctime() + "\n")
a = list(time.ctime())
print("Extracted current day is : " + a[8] + a[9])







print("\n\nQ.5- Extract date (ex : 11 in 11/01/2021) from the time.\n")

import datetime

a = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
'2011-11-03 18:21:26'

print("Current time is : " + a)

b = list(a)
print("Extracted date is : " + b[8] + b[9])








print("\n\nQ.6- Write a program to print time using localtime method.")

import time

print("\nUsing  time.localtime() :")
print(time.localtime())







print("\n\nQ.7- Find the factorial of a number input by user using math package functions.\n")

import math

num = int(input("Enter a integer to get its factorial : "))

print("Factorial of " + str(num) + " is : " + str(math.factorial(num)))








print("\n\nQ.8- Find the GCD of a number input by user using math package functions.\n")

import math

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

print("GCD of " + str(num1) + " and " + str(num2) + " is : " + str(math.gcd(num1,num2)))








print("\n\nQ.9- Use OS package and do the following tasks:") 
print("1. Get current working directory.")
print("2. Get the user environment.\n")


import os

print("\nCurrent Working Directory is :   " + os.getcwd())

print("User Environment is          :   " + os.environ['HOME'])

