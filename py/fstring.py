
# result = " hey my name is {0} i m {1}  old"
# name = "vishal"
# age = 22


# print(result.format(name,age))

# country ="india"
# name= "vishal"
# letter ="my name is {1} i m from  {0} "
# print(letter.format(country,name))
# print(f"my namei s {name} and i m from {country}")


# def squre(n):
#     '''squre'''
#     print(n**2)
# squre(5)   

# print(squre,__doc__)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# factorial(6)


# def func1():
#     try:
#         l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         i = int(input("Enter the index of the list: "))
#         print(l[i])
#         return 1
#     except IndexError:
#         print("Index out of range. Please enter a valid index.")
#         return 0
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
#         return 0
 

# # Example usage:
# result = func1()
# print("Result:", result)
# def divide(x,y):
#     try:
#         result = x / y
#         print("result is",result)
#     except ZeroDivisionError:
#         print("The division of Zero is nit allowved")
# numbertor =100
# divider =0
# divide(numbertor,divider)

# marks = [80, 90, 75, 85, 95]

# for index, mark in enumerate(marks, start=1):
#     print(mark)
#     if index == 3:
#         print("vishal")


# import os
# if(not os.path.exists("data")):
#     os.mkdir("data")
# for i in range(0,5):
#     os.mkdir(f"data/day{i+1}")            
        
# f = open("myfile","w")
# lines =["vishal rathore is the grate man"]
# f.writelines
# f.close()


# f =open("myfile")
# content = f.read()

# print(content)

# f.close()


# a=lambda x: x*2
# print(a(5))

# r =lambda  a:a+15

# print(r(10))

# r =lambda a ,b :a*b
# print(r(12,12))

# l = int(input("Enter the number of l: "))

# if l <= 0 or l > 5:
#     raise ValueError("Number should be between 1 and 5 (exclusive).")


def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    
    return mfx

@greet
def hello():
    print("Hello Vishal")

@greet
def add(a, b):
    print(a + b)

hello()
add(1, 3)
        
    
        