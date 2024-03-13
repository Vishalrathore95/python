#The if-else statement is used to execute both the true part and the false part of a given condition
#write a program to check the person is elegible for voting ARE NOT

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible for voting")
# else:
#     print("You are not eligible for voting")


#even are odd in python
# n= int(input("enter the number:"))
# if n%2==0:
#     print( n ,"even")
# else:
#     print(n,"odd")   


#number is divisible by  7 are not

# n= int(input("enter the number:"))
# if n%7==0:
#     print( n," divisible by 7")
# else:
#     print(n, "not divisible by 7")


# n= int(input("enter the number:"))
# if n%5==0:
#     print("HELLO")
# else:
#     print("BYE")

#ELECTRICITY BILL

# amt = 0
# num = int(input("enter the number:"))
# if num <=100:
#  amt =0
# if num >100 and num <=200:
#     amt  =(num-100)*5
# if num>200:
#     amt = 500+(num-200)*10  
#     print(amt)


#last digit of number
# num = int(input("enter the number:"))
# print("the last digit of number: " , num%10) 


#last digit of number is divisible by 3 are not
# n= int(input("enter the number:"))
# num = n%10

# if num%3==0:
#     print("the last digit of number is divisible by 3")
# else:
#     print("the last digit of number is not divisible by 3")

#price of bike

# tax = 0
# price = int(input("enter the price"))
# if price >100000:
#     tax = 15/100*price
#     if price >5000 and price  <=100000:
#         tax = 10/100*price 
#     else:
#         tax = 5/100*price
#         print(tax)

#check the year is leap year or not
# year =int(input("Enter a year :"))

# if year % 4 == 0:
#     print( year,"the year is leap year")
# else:
#     print("not a leap year")

# n = int(input("enter the number"))
# num =len(n)
# if(num != 3):
#     print(" enter three number digit")
# else:
#     print("middle digit is ", (int(n)%100//10))


# 
#prime number are not

# num = int(input("Enter the number: "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print("1 is not a prime number")

pa = int(input("Enter the number: "))
na = int(input("Enter the number: "))
per =(pa-na) *pa/100
if(per<=75):
    print("you are eligible for exam")
else:
    print("you are not eligible for exam")


