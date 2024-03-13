# str = "my name is vishal"
# print(str[1:6])
# print(str[1:9:3])
# print(str[-7:-2])



#METHODS IN STRINGS



#first letter ko capitale karti he
# str = "vishal"
# a =str.capitalize()
# print(a)


# str = "vishal"
# a =str.upper()
# print(a)


# str = "vishal"
# a =str.islower()
# print(a)


# converts the first character to  
# upper case and rest to lower case 
# text = 'geeKs For geEkS' 
# print("\nConverted String:") 
# print(text.title()) 

# lower() function to convert 
# string to lower case 

# text = 'geeKs For geEkS'
# print("\nConverted String:") 
# print(text.lower()) 

# print("\nConverted String:") 
# print(text.swapcase()) 
# capitalize(): Converts the first character to upper case
# string = "hello world"
# capitalized_string = string.capitalize()
# print(capitalized_string)  # Output: Hello world

# casefold(): Converts string into lower case
# string = "Hello World"
# lowercased_string = string.casefold()
# print(lowercased_string)  # Output: hello world


# # center(): Returns a centered string
# string = "hello"
# centered_string = string.center(10, '*')
# print(centered_string)  # Output: **hello***

# # count(): Returns the number of times a specified value occurs in a string
# string = "hello world"
# count_e = string.count('e')
# print(count_e)  # Output: 1


# # encode(): Returns an encoded version of the string
# string = "hello"
# encoded_string = string.encode()
# print(encoded_string)  # Output: b'hello'

# string = "hello world"
# ends_with_world = string.endswith("world")
# print(ends_with_world)  # Output: True


# # expandtabs(): Sets the tab size of the string
# string = "hello\tworld"
# expanded_string = string.expandtabs(10)
# print(expanded_string)  # Output: hello   world

# # find(): Searches the string for a specified value and returns the position of where it was found
# string = "hello world"
# position_of_o = string.find("o")
# print(position_of_o)  # Output: 4

# format(): Formats specified values in a string
# name = "Alice"
# age = 25
# formatted_string = "My name is {} and I am {} years old".format(name, age)
# print(formatted_string)  # Output: My name is Alice and I am 25 years old


# # format_map(): Formats specified values in a string
# person = {'name': 'Bob', 'age': 30}
# formatted_string = "My name is {name} and I am {age} years old".format_map(person)
# print(formatted_string)  # Output: My name is Bob and I am 30 years old


# # index(): Searches the string for a specified value and returns the position of where it was found
# string = "hello world"
# position_of_o = string.index("o")
# print(position_of_o)  # Output: 4

# # isalnum(): Returns True if all characters in the string are alphanumeric
# alphanumeric_string = "hello123"
# is_alnum = alphanumeric_string.isalnum()
# print(is_alnum)  # Output: True

# # isalpha(): Returns True if all characters in the string are in the alphabet
# alpha_string = "hello"
# is_alpha = alpha_string.isalpha()
# print(is_alpha)  # Output: True


# # isascii(): Returns True if all characters in the string are ascii characters
# ascii_string = "hello"
# is_ascii = ascii_string.isascii()
# print(is_ascii)  # Output: True

# # isdecimal(): Returns True if all characters in the string are decimals
# decimal_string = "12345"
# is_decimal = decimal_string.isdecimal()
# print(is_decimal)  # Output: True


# # isdigit(): Returns True if all characters in the string are digits
# digit_string = "12345"
# is_digit = digit_string.isdigit()
# print(is_digit)  # Output: True


# # isidentifier(): Returns True if the string is an identifier
# identifier = "variable_name"
# is_id = identifier.isidentifier()
# print(is_id)  # Output: True


# # islower(): Returns True if all characters in the string are lower case
# lowercase_string = "hello"
# is_lower = lowercase_string.islower()
# print(is_lower)  # Output: True


# # isnumeric(): Returns True if all characters in the string are numeric
# numeric_string = "12345"
# is_numeric = numeric_string.isnumeric()
# print(is_numeric)  # Output: True

# # isprintable(): Returns True if all characters in the string are printable
# printable_string = "hello\nworld"
# is_printable = printable_string.isprintable()
# print(is_printable)  # Output: False


#  #isspace(): Returns True if all characters in the string are whitespaces
# whitespace_string = "   "
# is_space = whitespace_string.isspace()
# print(is_space)  # Output: True

# # istitle(): Returns True if the string follows the rules of a title
# title_string = "Hello World"
# is_title = title_string.istitle()
# print(is_title)  # Output: True

# # isupper(): Returns True if all characters in the string are upper case
# uppercase_string = "HELLO"
# is_upper = uppercase_string.isupper()
# print(is_upper)  # Output: True

# # join(): Converts the elements of an iterable into a string
# words = ["Hello", "World"]
# joined_string = " ".join(words)
# print(joined_string)  # Output: Hello World


# # ljust(): Returns a left justified version of the string
# string = "hello"
# left_justified_string = string.ljust(10, '*')
# print(left_justified_string)  # Output: hello*****


# # lower(): Converts a string into lower case
# string = "HELLO"
# lowercased_string = string.lower()
# print(lowercased_string)  # Output: hello


# # lstrip(): Returns a left trim version of the string
# string = "   hello"
# left_trimmed_string = string.lstrip()
# print(left_trimmed_string)  # Output: hello


# # maketrans(): Returns a translation table to be used in translations
# translation_table = str.maketrans("aeiou", "12345")
# string = "hello"
# translated_string = string.translate(translation_table)
# print(translated_string)  # Output: h2ll4


# # partition(): Returns a tuple where the string is parted into three parts
# string = "hello world"
# partitioned_string = string.partition(" ")
# print(partitioned_string)  # Output: ('hello', ' ', 'world')

# # replace(): Returns a string where a specified value is replaced with a specified value
# string = "hello world"
# replaced_string = string.replace("world", "universe")
# print(replaced_string)  # Output: hello universe

# # rfind(): Searches the string for a specified value and returns the last position of where it was found
# string = "hello world"
# position_of_o = string.rfind("o")
# print(position_of_o)  # Output: 7

# # rindex(): Searches the string for a specified value and returns the last position of where it was found
# string = "hello world"
# position_of_o = string.rindex("o")
# print(position_of_o)  # Output: 7
# # rjust(): Returns a right justified version of the string
# string = "hello"
# right_justified_string = string.rjust(10, '*')
# print(right_justified_string)  # Output: *****hello


# # rpartition(): Returns a tuple where the string is parted into three parts
# string = "hello world"
# rpartitioned_string = string.rpartition(" ")
# print(rpartitioned_string)  # Output: ('hello', ' ', 'world')



#LOOPS IN STRING

str = "hello world"
i = 0

while i < len(str):
    print(str[i])
    i += 1

# for i in str:
#     print(i)

