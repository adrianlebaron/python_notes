# - Booleans > put false until publishe True or False
# - Numbers > tons of diferent
# - Strings > could be a "name" or full html document
# - Bytes and byte arrays > for implementing in a pixel level
# - None > to define a variable and set to none so you can change later. 
# - Lists > array on Ruby
# - Tuples similar as a list
# - Sets 
# - Dictionaries > hash data structure in Ruby

meal_completed = True
sub_total = 100
tip = sub_total * 0.2 #can be fractions
total = sub_total + tip
receipt = "Your total is" + str(total) #str(total) to use strings with numbers
print(total)
print(tip)
print(receipt)


