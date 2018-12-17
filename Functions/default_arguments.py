# Guide to Default Arguments in Python Functions video

# yep 
def greeting(name = 'Guest'): ## if you do not put anything it will return Guest
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Nope
def some_function(collection = []): ## do notuse mutable lists[] in default arguments
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())


def greeting(name = 'Guest', last = 'user'): ## if you do not put anything it will return Guest
  print(f'Hi {name} {last}!')

greeting()
greeting('Kristine')


def my_funct(positional_argument, default_argument = True, another argument, *adds all the rest):
  pass

  my_funct("postional argument", another_argument "named argument")