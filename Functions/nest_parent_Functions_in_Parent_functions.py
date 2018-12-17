# How to Nest Functions in Parent Functions in Python video

def full_name(first, last):
    return f'{first} {last}'

Kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
  print(f'Hi {neme}!')


greeting('Kristine', 'Hudgens')

def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')
