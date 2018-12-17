# Three Ways to Remove Elements from a Python List

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan') #typical use

print(users)

popped_user = users.pop()

print(popped_user)
print(users)

del users[0]

print(users)

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

del users[0]
popped_user = users.pop()
print(users)


users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']
print(user[1:-1])

one, *two, three = [1,2,3,4,5]
print(two)

# solution

def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content


html = ['<h1>', 'My content', '</h1>']

print(remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']

print(remove_first_and_last(other_content_to_clean))

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

del users[0]
del users[-1]
# users.pop(0)
# users.pop()
print(users)