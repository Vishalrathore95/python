#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values: {key: value}


# # Assuming you have variables 'name', 'age', and 'gender' defined elsewhere
# name = "John"
# age = 25
# gender = "Male"

# # Create a dictionary
# my_dict = {'name': name, 'age': age, 'gender': gender}

# # Modify the value associated with the 'name' key
# my_dict['name'] = "Vishal"

# # Print the updated 'name' value
# print(my_dict)

# dict ={'bikename':'r15','model':2005, 'color':'red', 'modelnumber':123456}
# dict['modelnumber' ]=987654
# print(dict)


# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict)

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # # x = thisdict["model"]
# # x = thisdict.get("model")
# x = thisdict.keys()
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# print(car)
# # # x = car.keys()
# # # x = car.values()
# # x = car.items()
# # print(x) #before the change

# # car["color"] = "white"
# # print(x) #after the change

# if "model" in car:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict["year"] = 2018
# thisdict.update({"year": 2020})
# thisdict["color"] = "red"
# thisdict.update({"color": "red"})

# thisdict.pop("model")
# thisdict.popitem()
# del thisdict["model"]
# thisdict.clear()
# for x in thisdict:
#   print(x)


# for x in thisdict.values():
#   print(x)

# for x in thisdict.keys():
#   print(x)



# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # mydict = thisdict.copy()
# mydict = dict(thisdict)
# print(mydict)


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)



