#The class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object. Some points on Python class: Classes are created by keyword class.

# class test :
#     def add(self,a,b):
#         print( 'adding',a+b)
#     def sub( self,a,b):
#         print('sub',a-b)
        
# obj=test()
# obj.add(5,3)
# obj.sub(7,2)

#
# import array
# for name in array.__dict__:
#     print(name)


# class student:
#     def __init__(self, id ,name, clas):
#         self.id = id
#         self.name = name
#         self.clas = clas
# student = student("123", 'vishal',"12th")  
# print(student.__dict__)   


# import builtins
# help(builtins.abs)
# print(builtins.abs(-155))

# import builtins

# # Use help() with builtins.abs (without parentheses)
# help(builtins.abs)

# # Now, let's use builtins.abs() with an argument
# result = builtins.abs(-155)
# print(result)
    
# def student_data(student_id,**kwargs):
#     print (f'\nStudent ID : {student_id}')    
#     if 'student_name' in kwargs:
#         print (f'Student Name :$ {kwargs['student_name']}')
#         if 'student_name' and 'student_class' in kwargs:
#             print(f'\nStudent Name :$ {kwargs['student_name']}') 
#             print(f'\nStudent Class :$ {kwargs['student_class']}')
# student_data (student_id="123", student_name="vishal", student_class="12")   
# student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')         
            
            
 
  
# class Student:
# print(type(Student))
# print(Student.__dict__.keys())
# print(Student.__module__)
# class Student:
#     pass  
# print(type(Student))
# print(Student.__dict__.keys())
# print(Student.__module__)
     
     
# class Student:
#     student_name = 'Terrance Morales'
#     marks = 93  
# print(f"Student Name: {getattr(Student, 'student_name')}")
# print(f"Marks: {getattr(Student, 'marks')}")
# setattr(Student, 'student_name', 'Angel Brooks')
# setattr(Student, 'marks', 95) 
# print(f"Student Name: {getattr(Student, 'student_name')}")
# print(f"Marks: {getattr(Student, 'marks')}")        