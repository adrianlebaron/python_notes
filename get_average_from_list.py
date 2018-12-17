# Get the Average from a List in Python video

#functools
#reduce
#sum / total num of elements
from functools import reduce
def get_average(num_list):
  total = reduce(
    (lambda total, element: total + element),
    num_list)
    
    return total / len(num_list)

num_list = [15, 15, 15, 18, 18, 19, 19, 19, 22, 22, 27, 24, 24,]


# def find_average(li):
#  return(sum(li) / len(li))

# num_list = [15, 15, 15, 18, 18, 19, 19, 19, 22, 22, 27, 24, 24,]
# print(find_average(num_list))
def find_average(li)
total = 0
for num in li:
  total += num
print(total / len(li))

find_average(,1 ,2 4, 5, 5, 5, 5, 5, 5, 5, 55, 100000)