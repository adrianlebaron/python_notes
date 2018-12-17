# Write a python program that takes a string and changes all occurrences of its first letter to a ‘$’, except for the first letter.
# Ex: “restart”
# # should return “resta$t” (edited)




def change_char(ltr1):
  char = ltr1[0]
  ltr1 = ltr1.replace(char, '$')
  ltr1 = char + ltr1[1:]

  return ltr1

print(change_char("AdrianDanLebaron"))



# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
# ex: “ABCD”
# should return “DBCA”
# ex: “windows”
# should return “sindoww” (edited)

def change_string(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_string('naD'))
print(change_string('119'))

change_string()


# Write a python program that sums (adds) all the items in a list
# ex: [1, 2, 3, 4]
# should return 10

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,-136]))

# Write a python program that takes a string and changes all occurrences of its first letter to a '$', except for the first letter.
# Ex: "restart"
# should return "resta$t" (edited)
# Write a method that takes a string as an argument
# Isolate the first letter of the word 
# Change all occurences of the first character to a $
# Return that string 
def change_letter(string):
  first_char = string[0]
  replaced_char = string.replace(first_char, '$')
  print(first_char + replaced_char[1:])

change_letter("restart")

`Victor Laucus notes`

# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
# ex: "ABCD"
# should return "DBCA"
# ex: "windows"
# should return "sindoww" (edited)
# Take in a string 
# Isolate the first and last letter of the given string
# create a new string with the first and last letter swapped 
# Middle letters in same order
def letter_reverser(string):
  first_let = string[:1]
  last_let = string[-1:]
  mid_let = string[1:-1]
  print(last_let + mid_let + first_let)

  # One line solution
  # print(string[-1:] + string[1:-1] + string[:1])

# letter_reverser("ABCD")


# Write a python program that sums (adds) all the items in a list
# ex: [1, 2, 3, 4]
# should return 10
# Write a function 
# Accept a list as an argument
# Iterate over the given list 
# Figure out a way to add all the elements and store the total 

# def sum_list(li):
#   # total = 0
#   # for x in li:
#   #   # total = total + x
#   #   total+= x
#   # print(total)
#   print(sum(li))


# sum_list([1, 2, 3, 4])

# oct 30

# 1) Write a Python program to sum all the items in a dictionary
# ex: { ‘data1’:100, ‘data2’:-54, ‘data3’:247 }
# output: 293

# seperate the values and add them up

payroll = {
  "angelita" : 900,
  "christian": 1000,
  "martha" : 500,
  "homar" : 1200,
}
print(sum(payroll.values()))



# 2) Write a Python program to append a list to the second list (add two lists together)
# ex: [1, 2, 3], [4, 5, 6]
# output: [1, 2, 3, 4, 5, 6]

one = []

print(one + two)


# 3) Write a Python program to merge two dictionaries together
# ex: {‘a’: 100, ‘b’: 200}, {‘x’: 300, ‘y’: 200}
# output: {‘x’: 300, ‘y’: 200, ‘a’: 100, ‘b’: 200}

# seperate dictionaries into a list add the two totals.
#cpmpiled dictionary

payroll = {
  "angelita" : "900",
  "christian": "1000",
  "martha" : "500",
  "homar" : "1200",
}
payroll_week_two ={
  "angelita" : "900",
  "christian": "2000",
  "martha" : "500",
  "homar" : "1200",
}


payroll.update (payroll.weektwo)


print(list_all + list_next)



# 4) Write a python program to check if a given key already exists in a dictionary
# ex: {‘x’: 300, ‘y’: 200, ‘a’: 100, ‘b’: 200}
# I want to see if the key `a` exists in the dictionary above. If it does return `Key exists` and if it doesn’t return `Key doesn't exist`

import math
payroll = {
  "angelita" : "900",
  "christian": "1000",
  "martha" : "500",
  "homar" : "1200",
}

employee = payroll.get('christian(key exist)', 'key does not exist')



print(employee)

`From Neil`

led 
# sum_thing = { 'data1':100, 'data2':-54, 'data3':247 }
# print(sum(sum_thing.values()))
​
# one = [1, 2, 3]
# two = [4, 5, 6]
​
# print(one + two)
​
# one = {'a': 100, 'b': 200}
# two = {'x': 300, 'y': 200}
​
# one.update(two)
​
# print(one)
​
one = {'x': 300, 'y': 200, 'a': 100, 'b': 200}
​
def identifier(key):
 if key in one:
  print("hallelueigh")
 else:
  print("no no no")
​
identifier("x")

Victor Laucas [4:27 PM] oct 30th
@channel Homework!

Watch and code along (take good notes!)
https://bottega.devcamp.com/12/guide/1483
https://bottega.devcamp.com/12/guide/1484

Code exercises: TRY TO SOLVE WITHOUT GOOGLE
Write a python program that asks the user for a word and reverse it
ex: Ask the user to input a word
User inputs word “Python”
program return “nohtyP”



def word_reverse():
  # while True:
    print('What is the word you would like to see backwords?')
    word = input()
    # if word == 'Adrian':
    print(f"here is your word backwords {word[::-1]} ")
    return False
    
word_reverse()
    

write a python program that prints all of the numbers from 0 - 20 except for 3, 9, and 14
*Might need to use a conditional :wink:
output: 0
1
2
4
5
6
7
8
10
11
12
13
15
16
17
18
19

for num in range(1, 20): #does not include the 10 you will be off by one
  print(num)
  if age < 25:
  print(f"I'm sorry, {age} is under 25 years old")

  forx in range(20):
    if (x == 3 or == 9 or == 14)
    print(x)

Write a Python program to concatenate all elements in a list into a string and return it.
input: [1, 5, 12, 2]
output: “15122”

string_one [08, 03, 1984]

input: [‘h’, ‘i’, 5]
output: “hi5"

def list_concat(li):
  string = ""
  for x in li:
   string += str(x)
  print(string)


for num in range(1, max_number): #does not include the 10 you will be off by one
  print(num)

# nums = range(0 ,101)
# # print(100 % 3)
# num = list(range(0, 101))
# thirds = (100 % 3) 
# print (thirds)
# fifths = (100 % 5)

# # print(num)
# def exchange():
#   if 
#    return('fizz')


# print()

def fizzbuzz():
  for x in range(1, 101):
    if (x % 3 == 0 and x % 5 == 0):
      print("fizzbuzz")
    elif (x % 3 == 0):
      print("fizz")
    elif (x % 5 == 0):
      print("buzz")
    else:
      print(x)
fizzbuzz()

# def fizz_buzz(max_num)
#  for num in range(1, max_num + 1):
#    if (num % 3 == 0 and num % 5 == 0):

