# How to Combine All Argument Types in a Single Python Function video

def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.
  (args)}, I hope that you're having a good {time_of_day}.")

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f'{key} -> {val}')


greeting('Morning',
         'Kristine', 'Hudgens',
         first = 'Empty dishwasher',
         second = 'Take pupper out',
         third = 'math homework')