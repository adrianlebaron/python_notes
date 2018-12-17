# Overview of Keyword Arguments in Python Functions video

def greeting(**kwargs):##keyword arguments
  print(kwargs)


greeting()
greeting(first = 'Kristine', last = 'Hudgens')

def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting()
greeting(first = 'Kristine', last = 'Hudgens')