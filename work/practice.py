# import operator
# from functools import reduce

"""dynamic_reducer([1, 2, 3], '+') # 6
dynamic_reducer([1, 2, 3], '-') # -
dynamic_reducer([1, 2, 3], '*') # 6
dynamic_reducer([1, 2, 3], '/') # -
"""

# def dynamic_reducer(collection, op):
#   operators = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv
#   }
  
#   return reduce((lambda total, element: operators[op](total, element)))

# print(dynamic_reducer)([1, 2, 3], '+') # 6
# print(dynamic_reducer)([1, 2, 3], '-') # -
# print(dynamic_reducer)([1, 2, 3], '*') # 6
# print(dynamic_reducer)([1, 2, 3], '/') # -


# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     return value

"""count the characters in a string"""

# from collections import Counter
# word = "Hello World"
# print(Counter((word)Total)
""" example 1"""
word = "Adrian Lebaron"
print(len(word))

"""example 2"""

name = 'Tauvi Bear is a stinker'
qtty=sum(len(x) for x in name.split())
print(qtty)

"""example 3 and 4"""
# >>> text = 'foo  bar  spam'
# >>> sum(len(x) for x in text.split())
#     10
# Or str.translate with len:

# >>> from string import whitespace
# >>> len(text.translate(None, whitespace)) #Handles all types of whitespace characters
# 10

# list = [1, 2, 3, 4]
# print(len(list)) 
# will print 4

# len() returns number of characters in a string INCLUDING the spaces

# If used on a list, returns number of items in the list (same goes for tuples)

name= "Tauvi Bear is a stinker"
word1= name[0:5]
word2= name[6:10]
word3= name[11:13]
word4= name[14:15]
word5= name[16:]

print(word4,word5)


"""Say you wanted to count the frequency of characters in a string:"""

# import itertools
# characters = sorted(“the quick brown fox jumps over the lazy dog”)
# analysis ={
# 	key: len(list(group)) \
# 	for key, group in itertools.groupby(characters)\
# 	if key != " "
# }
# print(analysis)
# {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 3, 'f': 1, 'g': 1, 'h': 2, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 4, 'p': 1, 'q': 1, 'r': 2, 's': 1, 't': 2, 'u': 2, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}

# could enter in the terminal

def main():
    full_name = str(input("Please enter in a sentence ")).split(" ")

    for x in full_name:
     print(len(x))

main ()


# Or str.translate with len:

# >>> from string import whitespace
# >>> len(text.translate(None, whitespace)) #Handles all types of whitespace characters



# ``````# Build a Manual Exponent Function

# from functools import reduce

# # manual_exponent=(2, 3):
#     computed_list = [num] * exp
# # manual_exponent=(10, 2):
#     computed_list = [num] * exp
# def reduce(function, iterable, initializer=None):
#   it= num * exp````````
  

    
#     # return (reduce(lamda total, element: total * element, computed_list))


# `````def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     `return value`````

#  `practice practice practice```
from functools import reduce

#  def manual_exponent(num, exp):
#      computed_list = [num] * exp
#      return (reduce(lambda total, element: total * element, computed_list))


#  print(manual_exponent(2, 3))
#  print(manual_exponent(10, 2))
#  print(manual_exponent(3, 3))
#  print(manual_exponent(10, 5))

def manual_exponent(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))
print(manual_exponent(3, 3))
print(manual_exponent(10, 5))

# Write a Python program to find the index of an item in a specified list.



birth_date = '8,3,19,84'
date = birth_date.split(',')
print(date)
print(date.index('3'))

# def index_of_item(li, item):     from Victor
#     print(li.index(item))
#     index_of_item([])



import random

foo = ['battery', 'correct', 'horse', 'staple']
secure_random = random.SystemRandom()
print(secure_random.choice(foo))



def remove_even(numbers) :
    new_list = []
    for i in range(0,len(numbers)-1) :
        if i % 2 != 0 :
            new_list.append(i)
    return new_list
l = [1,2,3,4,5,6,7,8,9,10]
print(remove_even(l))


# # write a program to select the odd numbers of a list
# def odd_num(li):
#   for x in li: 
#     if x % 2 == 1:
#       print(x)

# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_num([100, 234, 56, 23, 567, 234, 456, 123, 345, 2345 ,678])