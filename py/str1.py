# length = "vishalrathore"
# print(len(length))

# Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
# def char(str1):
#     dict ={}
#     for i in str1:
#         keys = dict.keys()
#         if i in keys:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     return dict
# print(char("hello"))
#  Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String


# # def string(str):
#     if len(str) < 2:
#         return ''
#     return str[0:2] + str[-2:]

# print(string("hello vishal"))
# print(string("hello"))
# print(string(" vishal"))


char ="resert"

new = char.replace("r","$")
print(new)



