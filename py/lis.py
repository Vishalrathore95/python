#A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ] .


list = [10, 22, 22.2 ,"vishal",True ,False]
# list[2] = "rathore"
# print(list)

# for i in  list:
#     print(i)
# i =0 
# while  i<=len(list):
#     print(list[i])
#     i+=1


# # print(list[2: 5:2])
# # print(list[-6: -3])
# list.append(60)
# print(list)
# append()
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
# # Comment: append() adds the specified element at the end of the list.

# # clear()
# fruits = ["apple", "banana", "cherry"]
# fruits.clear()
# print(fruits)  # Output: []
# # Comment: clear() removes all elements from the list.

# # copy()
# fruits = ["apple", "banana", "cherry"]
# fruits_copy = fruits.copy()
# print(fruits_copy)  # Output: ['apple', 'banana', 'cherry']
# # Comment: copy() creates a shallow copy of the list.


# # count()
# numbers = [1, 2, 3, 1, 4, 1]
# count = numbers.count(1)
# print(count)  # Output: 3
# # Comment: count() returns the number of occurrences of the specified value in the list.

# # extend()
# fruits = ["apple", "banana", "cherry"]
# more_fruits = ["orange", "kiwi"]
# fruits.extend(more_fruits)
# print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'kiwi']
# # Comment: extend() adds the elements of another list to the end of the current list.

# # index()
# fruits = ["apple", "banana", "cherry"]
# index = fruits.index("banana")
# print(index)  # Output: 1
# # Comment: index() returns the index of the first occurrence of the specified value.

# # insert()
# fruits = ["apple", "banana", "cherry"]
# fruits.insert(2, "orange")
# print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']
# # Comment: insert() adds an element at the specified position in the list.

#  #pop()
# fruits = ["apple", "banana", "cherry"]
# popped_fruit = fruits.pop(0)
# print(popped_fruit)  # Output: 'banana'
# # Comment: pop() removes and returns the element at the specified position.

# # remove()
# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)  # Output: ['apple', 'cherry']
# # Comment: remove() removes the first occurrence of the specified value from the list.

# # reverse()
# fruits = ["apple", "banana", "cherry"]
# fruits.reverse()
# print(fruits)  # Output: ['cherry', 'banana', 'apple']
# # Comment: reverse() reverses the order of the elements in the list.

# # sort()
# numbers = [4, 2, 7, 1, 5]
# numbers.sort()
# print(numbers)  # Output: [1, 2, 4, 5, 7]
# # Comment: sort() arranges the elements of the list in ascending order by default.