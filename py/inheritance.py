#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

#
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def printname(self):
#         print(self.name)
#         print(self.age)
# p =person("vishal",22) 
# p.printname           
# single imheritance
#Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.

# class test:
#     def vihical(self):
#         print("vihical")
#     def horn(self):
#         print("horn")

# class car(test):   #car class is inheriting from test class
#     def color(self):
#         print("color of car")
#     def drive(self):
#          print("drive") 
# t = car()
# t.vihical()
# t.horn()
# t.color()
# t.drive()         


#multileval inheritance
#Multilevel Inheritance in Python is a type of Inheritance that involves inheriting a class that has already inherited some other class
# class test:
#     def vihical(self):
#         print("vihical")
#     def drive(self):
#         print("drive")
# class car(test):
#     def color(self):
#         print("color of car")
#     def horn(self):
#         print("horn")
# class car1(car):
#     def drive1(self): 
#         print("every one can drive a car ")
# c =car1()
# c.vihical()
# c.drive()
# c.color()
# c.drive1()
# c.horn()  


#multiple inheritance
#f a child class is inheriting the properties of a single other class, we call it single inheritance. However, if a child class inherits from more than one class, i.e. this child class is derived from multiple classes, we call it multiple inheritance in PythON
# class test:
#     def vihical(self):
#         print("vihical") 
# class test1:
#     def horn(self):
#         print("horn")
# class demo:
#     def color(self):
#         print("color of car")
# class demo2( demo ,test,test1):
#     def drive(self):
#         print("drive")                
# d =demo2()
# d.vihical()
# d.color()
# d.horn()
# d.drive()
            
            
            
#heriechical inheritance
#f multiple derived classes are created from the same base, this kind of Inheritance is known as hierarchical inheritance. 

# class drive():
#     def vehicle(self):
#         print("vehicle")

# class demo(drive):
#     def color(self):
#         print("car has a color")

# class demo2():
#     def horn(self):
#         print("every car has a horn")

# # Create an instance of demo, which inherits from drive
# d = demo()
# d.vehicle()  # Access the method from the drive class
# d.color()    # Access the method from the demo class

# # Create an instance of demo2
# t = demo2()
# t.horn()  # Access the method from the demo2 class
         
          
          
#Hybrid Inheritance is a blend of more than one type of inheritance. The class is derived from the two classes as in the multiple inheritance. However, one of the parent classes is not the base class. It is a derived class. This feature enables the user to utilize the feature of inheritance at its best.
# class School:
#     def func1(self):
#         print("This is the function for func1")

# class Student1(School):
#     def func2(self):
#         print("Student 1 in school")

# class Student2(School):
#     def func3(self):
#         print("Student 2 in school")

# class Student3(School):
#     def func4(self):
#         print("Student 3 in school")

# # Create instances of each class
# student1_instance = Student1()
# student2_instance = Student2()
# student3_instance = Student3()

# # Call methods for each student
# student1_instance.func1()  # Call func1 from the base class
# student1_instance.func2()  # Call func2 from Student1

# student2_instance.func1()  # Call func1 from the base class
# student2_instance.func3()  # Call func3 from Student2

# student3_instance.func1()  # Call func1 from the base class
# student3_instance.func4()  # Call func4 from Student3


        
   
# Import required modules
from abc import ABC, abstractmethod
 
# Create Abstract base class
class Car(ABC):
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
     
  # Create abstract method      
  @abstractmethod
  def printDetails(self):
    pass
   
  # Create concrete method
  def accelerate(self):
    print("speed up ...")
   
  def break_applied(self):
    print("Car stop")
     
# Create a child class
class Hatchback(Car):
   
  def printDetails(self):
    print("Brand:", self.brand)
    print("Model:", self.model)
    print("Year:", self.year)
   
  def Sunroof(self):
    print("Not having this feature")
     
# Create a child class
class Suv(Car):
   
  def printDetails(self):
    print("Brand:", self.brand)
    print("Model:", self.model)
    print("Year:", self.year)
   
  def Sunroof(self):
    print("Available")
 
     
car1 = Hatchback("Maruti", "Alto", "2022")
 
car1.printDetails()
car1.accelerate()               
                                            