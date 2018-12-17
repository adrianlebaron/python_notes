# Introduction to Python Tuples

# List: [] # List: mutable
# Dictionary: {} # Immutable but can add Tuple strings
# Tuple: () # Tuple: immutable 
# string: "",'' are immutable as well 

# List: mutable
# Tuple: immutable 


post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

#post.sort() # cannot do this on on a tuple () but yes on a list

# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)


# Guide to Slices in Python Tuples video

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

print(post[1::2])

# pseudocoding exercise

# using the fantastically constructed programming language 
# "english" write a program that will tell our N31L bot to make a PB & J

get bread from fridge set on counter
get peanut butter from fridge set on counter open jar put lid aside
get jelly from fridge put on counter open jar put lid aside
get butter knife from fridge hold in 3rd hand 
seperate both slices of bread on the counter
dip butter knife in peanut butter jar spread on 1 slice 
dip butter knife in peanut butter jar spread on other slice 
pick up both slices of bread smash together

