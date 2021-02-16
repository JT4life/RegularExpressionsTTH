import re


names_file = open("names.txt", encoding="utf-8")  # Is a pointer to the file
data = names_file.read()  # puts all the contents of names file into data
names_file.close()  # No longer pointing to it

# print(data)

# print(re.match(r'Love', data))  # r means raw string
# print(re.match(r'Kenneth', data))  # match only matches the beginning of string, which prints None
# print(re.search(r'Kenneth', data))  # to match somewhere in the string use search

# can use variables as names to search e.g.
# first_name = r'Kenneth'
#
# print(re.search(first_name, data))

print(re.match(r'\w, \w', data))  # prints None
print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))  #  Parenthesis define a group so you have to escape them \

# Using {} to find exactly amount looking for 0-9
print(re.search(r'\(\d{3}\) \d{3}-\d{4}', data))
# <re.Match object; span=(40, 54), match='(555) 555-5555'> prints first line matching

# Since we have some numbers without parenthesis we can make it optional by adding ? use findall
print(re.findall(r'\(?\d{3}\)? \d{3}-\d{4}', data))

# Since we also have some hyphen and space we can do this
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

print(re.search(r'\w+, \w+', data))  # find one or more of any character in Unicode, and then again 1 or more word character

print(re.findall(r'\w+, \w+', data))  # find all of our names

# We are missing Tim with the above code so let's try it with *
print(re.findall(r'\w*, \w+', data))