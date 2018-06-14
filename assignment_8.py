print("Q.1- Create a circle class and initialize it with radius.")
print("Make two methods getArea and getCircumference inside this class.\n")

class Circle():
    
    def __init__(self,radius):
        self.radius = radius
        
    def  getArea(self):
        print("Area is : " + str(3.14*self.radius*self.radius))
    
    def getCircumference(self):
        print("Circumference is : " + str(self.radius*2*3.14))


A = Circle(float(input("Enter radius : ")))
A.getArea()
A.getCircumference()







print("\n\nQ.2- Create a Student class and initialize it with name and roll number.")
print("Make methods to :")
print("1. Display - It should display all informations of the student.\n")


class Student():
    
    def __init__(self,name,roll):
        self.name = name
        self.roll= roll

    def Display(self):
        print(self.name)
        print(self.roll)
        
A = Student(input("Enter name of student : "), input("Enter his/her roll no : "))
A.Display()









print("\n\nQ.3- Create a Temprature class.")
print("Make two methods :")
print("1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.")
print("2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.\n")


class Temperature():

    def  convertFahrenhiet(self,celsius):
        print("Temperature in Fahrenhiet is : " + str((celsius*(9/5))+32))
        
    def convertCelsius(self,farenhiet):
        print("Temperature in Celsius is : " + str((farenhiet-32)*(5/9)))

A = Temperature()
A.convertFahrenhiet(int(input("Enter temperature in Celcius : ")))
A.convertCelsius(int(input("Enter temperature in Fahrenhiet : ")))









print("\n\nQ.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings.")
print("Make methods to")
print("1. Display -->  Display the details.")
print("2. Update  -->  Update the movie details.")


class MovieDetails():

    def __init__(self, Moviename, Artistname, Yearofrelease, Ratings):
        self.Moviename = Moviename
        self.Artistname = Artistname
        self.Yearofrelease = Yearofrelease
        self.Ratings = Ratings

    def Display(self):
        print("\n\nMovie name is      : " + str(self.Moviename))
        print("Artist name is     : " + str(self.Artistname))
        print("Year of Release is : " + str(self.Yearofrelease))
        print("Ratings is         : " + str(self.Ratings) + "\n\n")

    def Update(self):
        self.Moviename = input("Enter updated Movie name      : ")
        self.Artistname = input("Enter updated Artist name     : ")
        self.Yearofrelease = input("Enter updated Year of release : ")
        self.Ratings = input("Enter updated Ratings         : ")

A = MovieDetails('3 IDIOTS','AAMIR KHAN', '2008', '87')
A.Display()

A.Update()
A.Display()











print("\n\nQ.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods :")
print("1. Display expenditure and savings.")
print("2. Calculate total salary.")
print("3. Display salary.")


class Expenditure():

    def __init__(self, expenditure, savings):
        self.expenditure = expenditure
        self.savings = savings

    def Display(self):
        print("\n\nExpenditure is  : " + str(self.expenditure))
        print("Savings is      : " + str(self.savings))
        
    def Cal_TotalSalary(self):
        Expenditure.totalsalary = self.expenditure + self.savings

    def Display_TotalSalary(self):
        print("Total Salary is : " + str(self.totalsalary))

A = Expenditure(input("\n\nEnter Expenditure : "), input("Enter Savings     : "))
A.Display()

A.Cal_TotalSalary()
A.Display_TotalSalary()