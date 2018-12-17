# Introduction to Using List Comprehension in Python

num_list = range(1, 11)
cubed_nums = []

# for num in num_list:
#   cubed_nums.append(num ** 3) ##this is slower

cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)

even_numbers = []

# for num in num_list:
#   if num % 2 == 0:
#     even_numbers.append(num) ## not list comprehensive

even_numbers = [num for num in num_list if num % 2 == 0]

print(even_numbers)