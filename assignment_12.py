print("Q.1- Name and handle the exception occured in the following program : \n")


a=3
try:
    if a<4:
        a = a/(a-3)
        print(a)

except:
     print("IdentationError: Resolved")







print("\n\nQ.2- Name and handle the exception occurred in the following program :\n")

l = [1, 2, 3]

try:
    print(l[3])

except:
    print("IndexError Resolved")







print("\n\nQ.3- What will be the output of the following code :\n")

'''
CODE:
----------------------------------
try:
    raise NameError("Hi there")

except NameError:
    print("An exception")
----------------------------------
'''

print("An exception")







print("\n\nQ.4- What will be the output of the following code :\n")

'''
CODE:
------------------------------------------
# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
------------------------------------------
'''

print("-5.0")
print("a/b result is 0")






print("\n\nQ.5- Write a program to show and handle following exceptions :")
print("     1. ImportError")
print("     2. ValueError")
print("     3. IndexError\n")



try:
    raise IndexError
except IndexError:
    print("IndexError  Resolved")


try:
    raise ImportError
except ImportError:
    print("ImportError Resolved")


try:
    raise ValueError
except ValueError:
    print("ValueError  Resolved")








print("\n\nQ.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.")
print("The code must keep taking input till the user enters the appropriate age number(less than 18).\n")


class Error(Exception):
    pass

class AgeTooSmallError(Error):
    def __init__(self):
        print("AgeTooSmallError: WARNING")

while True:
    val = int(input("Enter age: "))
    try:
        if val < 18:
            raise AgeTooSmallError
        else:
            print("Your age: ",val)
            break
    except AgeTooSmallError:
        print("Age is less than 18. Enter value equal to or greater than 18. Try again!!")

print("........YOU ARE OUT OF THE LOOP NOW........")