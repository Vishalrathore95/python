#A for loop in Python is a control flow statement that is used to repeatedly execute a group of statements as long as the condition is satisfied

#for variable in range
''' range(stop)
 range(start, stop)
 range(start, stop, step)'''

# for i in range(20,2, -2):
#     print(i)

# num=int(input("enter the number od table"))
# for  i in range(1,11):
#     print(num*i)

for i in range(5,1,-1):
    for j in range(1 ,i+1):
        print(i,end="")
    print()