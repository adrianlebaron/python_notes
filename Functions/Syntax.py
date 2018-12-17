# Basic Syntax for Creating Python Functions Video

def full_name(first, last): ##full_name is function not variable
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')

def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')
full_name(first = 'Kristine', last = 'Hudgens')###just use named arguments if using more then 2 Arguments
full_name(last = 'Hudgens', first = 'Kristine')

def auth(email, password):
  if email == 'kristine@hudgens.com' and password == 'secret':
    print('You are authorized')
  else:
    print('You are not authorized')


auth('kristine@hudgens.com', 'asdf')

def hundred():
  for num in range(1, 101): ##if you want to go backwords 
    print(num)


hundred()

def counter(max_value):
  for num in range(1, max_value):
    print(num)


counter(501)

def my_funct(positional_argument, default_argument = True, another argument, *args all the rest):
  pass

  my_funct("postional argument", another_argument "named argument")


int("1")#converts 1 to  integer