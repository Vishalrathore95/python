#INTILIZATION
# WHILE(BE/CONDITION)
#INCREASEMENT /DECREAMENT

#A while loop is a control flow statement which repeatedly executes a block of code until the condition is satisfied. It stops executing the block only if the condition fails. One should use a 'while' loop when one needs to perform a repeated operation, but doesn't know in advance how many iterations would be needed.


#PRINT FIRST 10 EVEN NUMBER
#PRINT FIRST 10 ODD NUMBER
#PRINT FIRST 10 NATURAL NUMBER
#PRINT FIRST 10 WHOLE NUMBER


# a =0
# while(a<10):
#      a+=1
#      print(a)

# a =0
# while(a<20):
#      a+=2
#      print(a)


# a =0
# while(a<10):
#      a+=1
#      print(a)
# a =0
# while(a<10):
#      a+=1
#      print(a)
# PRINT FIRST 10 INTERGER AND THEIRE SQURE
# num =0
# while(num<10):
#     num =num+1
#     print(num,"\t", num**2)


#write  the program for following series 10 ,20 ,30,....300
# i=10
# while(i<=300):
#     i+=10
#     print(i,end="")

# i=300
# while(i >10):
#     i-=10
#     print(i,"\t",end="")


# i=10
# while(i>0):
#     i-=1
#     print(i,"\t",end="")

# i=0
# sum =0
# while(i>=1):
#     sum = sum + i
#     i = i-1
#     print(sum)
     
     
     
# i=2
# sum =0
# while(i<=20):
#     sum = sum + i
#     i = i+2
#     print(sum)
  
# i = 1   
# num = int(input("Enter the number of the table: "))

# while i <= 10:
#     print(num, "*", i, "=", num * i)
#     i = i + 1


# i =0
# j =49
# while(i<=49 and i>=1):
#     i+=1
#     j-=1
#     print(i,"\t",j)
# i =1
# f = 5
# while(1<=f):
#     if(f%2==0):
#      i= i +1

# num = int(input("enter the number"))
# r =0 
# rnum =0
# while(num !=0):
#     r = num %10   # इससे बची हुई संख्या का अंतिम अंक मिलता है
#     rnum = rnum*10 + r  # पलटी हुई संख्या को बनाने के लिए पिछली पलटी हुई संख्या को 10 से मultiply करके और नए अंक को जोड़कर मिलती है
#     num = num//10  # बची हुई संख्या को 10 से भाग करके एक अंक कम करते हैं
#     print("reverce  number is :", rnum)
    
nu = int(input("enter the number"))  
f =1
i =1
while(i<=nu):
    f  =f*i
    i = i+1
    print("factorial is :", f)   
    

             
    
    
        