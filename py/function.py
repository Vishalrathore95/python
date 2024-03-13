#A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.


# def  add(a,b):
#     print( 'adding',a+b)
# add(2,3)    
# def  sub(a,b):
#     print( 'sub',a-b)
# sub(2,3)    

# def mul(a,b):
#     print( 'mul',a*b)


# def div(a,b):
#     print( 'divide',a/b)
# div(2,4)

# def mod(a,b):
#     print( 'modulas',a%b)
# mod(2,4)
# def cla():
#     a =int(input("enter the value of  a::"))
#     b =int(input("enter the value of  b::"))
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a//b)
#     print(a%b)
#     print(a**b)
# cla()
# cla()
# cla()
# cla()
# cla()
# cla()
# cla()


# def person(name ,age):
#     print("name is name",name)
#     print("age is",age)
    
# person(name="vishal", age =22)    

# def person(name ,age=21):
#     print("name is name",name)
#     print("age is",age)
    
# person(name="vishal") 



# def person(name ,age=21):
#     print("name is name",name)
#     print("age is",age)
    
# person(name="vishal" age =22)

# def add(a,*b):
#     print('THE value of a is',a)
#     print('THE value of b is',b)
#     print(a + sum(b))
# add(12,*(33,445,55,33,11,1,2,3))


#Write a Python function to find the maximum of three numbers.


# # Define a function that returns the maximum of two numbers
# def max_of_two(x,y):
#      # Check if x is greater than y
#     if x >y:
#           # If x is greater, return x
#         return x
#         # If y is greater or equal to x, return y
#     return y 
#  # Define a function that returns the maximum of three numbers
# def max_of_three(x,y,z):
    
#        # Call max_of_two function to find the maximum of y and z,
#     # then compare it with x to find the overall maximum
#     return max_of_two(x,max_of_two(y,z))

# # Print the result of calling max_of_three function with arguments 3, 6, and -5
# print(max_of_three(3,6,-5))


#Write a Python function to sum all the numbers in a list.

# def sum_numbers(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total

# numbers_list = [2, 4, 5, 6, 7, 8]
# print(sum_numbers(numbers_list))


# def mul(numbers):
#     total = 1
#     for x in numbers:
#         total = total * x
#     return total

# numbers_list = [2, 4, 5, 6, 7, 8]
# print(mul(numbers_list))
#Write a Python program to reverse a string.

#Sample String: "1234abcd"
#Expected Output: "dcba4321"
# def reverse():
#     a = '1234abcd'
#     # b = a[::-1]
#     print(a[::-1] )
    
# reverse()   
#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


# def factorial():
#     n = int(input("Enter a number: "))
#     total = 1
#     for i in range(1,n+1):
#         total = total * i
#     print(total)
# factorial()

# Write a Python function to check whether a number falls within a given range

# def range1(n):
#        if n in range(3,9):
#            print(n," is in range 3-9")
#        else:
#            print(n," is not in range 3-9")    
# range1(6)
# range1(11)   

#Write a Python function that takes a list and returns a new list with distinct elements from the first list.

# def unique_list(l):
#     x =[]
#     for i in l:
#         if i not in x:
#             x.append(i)
#     return x

# print(unique_list([1,2,3,3,3,3,3,3,3,3,4,5,6,7,8,9,6,6,6,6,6,10]))

# def prime(n):
#      if n==1: 
#          return False
#      elif(n==2):
#          return True
#      else:
#          for i in range(2,n):
#              if(n%i==0):
#                  return False
#              return True
# print(prime(9))        
   
   
# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True

# print(prime(9))


# def even(l):
#     enum =[]
#     for i in l:
#         if i % 2 == 0:
#             enum.append(i)
#     return enum

# def odd(l):
#     onum = []
#     for i in l:
#         if i % 2 != 0:
#             onum.append(i)
#     return onum

# print("Even numbers are :",even([1,2,3,4,5,6]))
# print("odd numbers are :",odd([1,2,3,4,5,6]))
    
   