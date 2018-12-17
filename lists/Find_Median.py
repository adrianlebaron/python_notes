# How to Find the Median of a Python List with an Odd Number of Numbers

#only work with odd number of elements
"""
Tools
- math library
- sorted function
- list slicing
- computations
"""

[0,1,2,3,4,5,6,7,8,9,10]

(100 / 42)

first i need to sort 
then devide in 2
then seperate

string = "10, 7, 0 , 5, 6, 4, 2, 1, 3, 8, 9"
sorted = string.sort

import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

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

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)


# import statistics
# print(statistics)median