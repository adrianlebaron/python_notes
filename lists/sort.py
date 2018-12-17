# How to Sort Lists in Python

tags = ['python', 'development', 'tutorials', 'code']

print(tags)

tags.sort()

print(tags)

tags.sort(reverse=True) #shows newest first

print(tags)

totals = [234, 1, 543, 2345]

totals.sort(reverse=True)

print(totals)

# Guide to the sorted Function in Python

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]
#sale_prices.sort() will work but changes the entire structure better to pass as variable but it wont print 

sorted_list = sorted(sale_prices, reverse=True)

print(sorted_list)

# `print (f" {varable })`

#learn the difference between a function and a method 