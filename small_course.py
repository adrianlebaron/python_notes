# https://www.udemy.com/python-video-workbook/learn/v4/t/lecture/6210162?start=0
my_range = range(1,200)
print 10 * x in my_range

print(list(map(str my_range)))

exercise 14
# Question: Complete the script so that it removes duplicate items from list a .

# a = ["1", 1, "1", 2]
# Expected output: 

#   ['1', 2, 1] 

# Hint 1: Sets are datatypes where duplicates are not allowed.

Explanation 1: 
Answer 1: 

a = ["1", 1, "1", 2]
a = list(set(a))
print(a)

We used a set  function to convert the list to a set which would intermediately produce {'1', 1, 2}  with no duplicates because set objects cannot contain duplicates. Then using list  we converted the set back to a list. The drawback here is that the original order of the items is lost. If you need to preserve the order you may want to use the solution in Answer 2 below.

Answer 2:

from collections import OrderedDict ### prefered
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)
Explanation 2:

Ordered dictionaries are another data type in Python that unlike sets and normal dictionaries they preserve the order of the items. Here OrderedDict.fromkeys(a)  would produce an OrderedDict  like [('1', None), (1, None), (2, None)] . Then we would convert that OrderedDict  to a list.

Answer 3:

a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
Explanation 3:

This is another solution that would preserve the original order. We go through all items of the original list and append them to the new list if they have not been appended before. The downside of this is the operation can take a lot of time if the list is large as we need to access both lists and also perform a conditional in each iteration.

Exercise 15 for reference: 

Create a dictionary that contains the keys a  and b  and their respective values 1  and 2 .

##solution
Answer 1: 

d = {"a": 1, "b": 2}
Explanation 1: 

Using curly brackets is one way to create a dictionary.

Answer 2:

d = dict(a = 1, b = 2)
Explanation 2:

A dict  function is another way to create a dictionary. dict  is also used to convert other objects to a dictionary.

# Exercise 16: Solution
Section 1, Lecture 37

Exercise for reference: 

Please complete the script so that it prints out the value of key b  .

d = {"a": 1, "b": 2}
# Answer: 

d = {"a": 1, "b": 2}
print(d["b"])
Explanation: 

As you see, accessing dictionary values follows the same syntax as accessing list items. The difference is that lists have indexes, while dictionaries have keys which you create by yourself.

# Exercise 17: Solution
Section 1, Lecture 39

Exercise for reference: 

Calculate the sum of the values of keys a  and b .

d = {"a": 1, "b": 2, "c": 3}
# Answer: 

d = {"a": 1, "b": 2, "c": 3}
print(d["b"] + d["a"])
Explanation: 

It's as easy as that. However, if you want to do the sum of all dictionary values you need to take another approach instead of accessing all values one by one. We're going through that approach later on in another exercise.

# Exercise 18: Solution
Section 1, Lecture 41

Exercise for reference: 

d = {"Name": "John", "Surname": "Smith"}
print(d["Smith"])
# Answer:

There is no key Smith  in the dictionary. Smith  is a value. You want to use Surname  if you want to access Smith :

print(d["Surname"])
Explanation: 

A KeyError always means Python could not find a key with the name shown next to KeyError (e.g. Smith ).

# Exercise 19: Solution
Section 1, Lecture 43

Exercise for reference: 

Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.

d = {"a": 1, "b": 2}
# Answer: 

d = {"a": 1, "b": 2}
d["c"] = 3
print(d)
Explanation: 

Adding pairs of keys and values is straightforward as you can see. Note though that you cannot fix the order of the dictionary items. Dictionaries are unordered collections of items.

# my answer to below
# d = {"a": 1, "b": 2, "c": 3}
# print sum(d.values())
# forgot parentesis in the print function
# Exercise 20: Solution
Section 1, Lecture 45

Exercise for reference: 

Calculate the sum of all dictionary values.

d = {"a": 1, "b": 2, "c": 3}
Answer: 

d = {"a": 1, "b": 2, "c": 3}
print(sum(d.values()))
Explanation: 

d.values()  returns a list-like dict_values  object while the sum  function calculates the sum of the dict_values  items.

# Exercise 21: Solution
Section 1, Lecture 47
a
Exercise for reference:                                                                                                                                                                                                                                                                                                                                                                     

Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}
# Answer: 

d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)
Explanation: 

Here we're using a dictionary comprehension. The comprehension is the expression inside dict() . The comprehension iterates through the existing dictionary items and if an item is less or equal to 1,the item is added to a new dict. This new dict is assigned to the existing variable d  so we end up with a filtered dictionary in d.