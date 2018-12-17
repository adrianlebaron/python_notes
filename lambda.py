 """reduce defines the total
 and recycles itd
 
 = lambda x, y : x + y"""

 from functools import reduce

 def population (Humans, sex):
     decendants = [humans] * sex
     return (reduce(lambda kids, couples: kids * couples, decendants))


 print(decendants(2, 3))
 print(decendants(10, 2))
 print(decendants(3, 3))
 print(decendants(10, 5))


 full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))


full_name =