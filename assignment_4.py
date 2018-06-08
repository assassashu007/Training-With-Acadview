print("Q.1- Take an input year from user and decide whether it is a leap year or not.")

year = int(input("Enter a year format is XXXX : "))
print("Year enterd is : " + str(year))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(str(year) + " is a leap year.")
       else:
           print(str(year) + " is not a leap year.")
   else:
       print(str(year) + " is a leap year.")
else:
   print(str(year) + " is not a leap year.")
                






print("\n\nQ.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.")

length = int(input("Enter length : "))
breath = int(input("Enter breath : "))

if length == breath:
        print("Dimentions are of SQUARE.")
else:
        print("Dimentions are of RECTANGLE.")







print("\n\nQ.3- Take the input age of 3 people and determine oldest and youngest among them.")

a=int(input("Enter person 1 age : "))
b=int(input("Enter person 2 age : "))
c=int(input("Enter person 3 age : "))

if a>b:
        if a>c:
                print("Person 1 is oldest.")
        else:
                print("Person 3 is oldest.")
if b>a:
        if b>c:
                print("Person 2 is oldest.")
        else:
                print("Person 3 is oldest.")

if a<b:
        if a<c:
                print("Person 1 is youngest.")
        else:
                print("Person 3 is youngest.")
if b<a:
        if b<c:
                print("Person 2 is youngest.")
        else:
                print("Person 3 is youngest.")






print("\n\nQ.4-Prize on points")

points = int(input("Enter points between 1 - 200 : "))

if points in range(1,201):
        if points <= 50:
                print("Sorry! No prize this time.")
        elif points <= 150:
                print("Congratulations! You won a Wodden Dog!")
        elif points <= 180:
                print("Congratulations! You won a Book!")
        else:
                print("Congratulations! You won a Chocolates!")
else:
        print("INVALID POINTS ENTERED")




print("\n\nQ.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. ")


quantity = int(input("Enter the quantity of items buyed : "))
cost = quantity * 100
if quantity > 1000:
        discount = 0.1 * cost
        cost = cost - discount
        print("Cost after discount is : " + str(cost))
else:
        print("NO DISCOUNT! Cost is : " + str(cost))
