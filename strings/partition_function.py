heading ="python: An Introduction this is"

header, _, subheader = heading.partition(': ')

print(header)
print(_)    #this is a throw away variable
print(subheader)


# Guide to the Python split Function /Video

tags = 'python,coding,programing,development'

list_of_tags = tags.split(',')

print(list_of_tags)

heading ="python: An Introduction this is"

header_list = heading.split(': ')

print(header)
print(_)    #this is a throw away variable
print(subheader)

""" use .split   more then .partition """

# How to Check if Strings Represent Numbers or Alphanumeric Characters in Python

api_data = '5'
greeting = 'Hi' #counts spaces as numeric not Alpha

print(api_data.isalpha())
print(greeting.isalpha())

print(api_data.isnumeric())
print(greeting.isnumeric())