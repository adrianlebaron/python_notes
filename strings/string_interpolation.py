name = 'Kristine'
greeting = f'Hi {name}'
print(greeting)


name = 'Kristine'
greeting = f'Hi {2 + 2}' #f is format python will look for curly brackets
print(greeting)

name = 'Kristine'
greeting = f'Hi {{name}}' #double brackets will print out brackets
print(greeting)

name = 'Kristine'
product = 'Python elearning course'

email_content = f"""
Hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""

print(email_content)

name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Jordan'

greeting = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old. - {3}".format(name, age, product, 'Adrian Lebaron')

greeting = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}"

print(greeting)

# str.format(*args, **kwargs)
# Perform a string formatting operation. The string on which this method is called can contain literal text or >replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional >argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is >replaced with the string value of the corresponding argument.

# Finding a Substring in Python with: Find, Index, and In



# query = sentence.find('quick') 
# query = sentence.index('quick')

# sentence = 'The quick brown fox jumped over the lazy dog.'

# query = sentence.find('oops')
# query_two = sentence.index('oops')                                       """not working"""
# print(query)
# print(query_two)

# query = 'oops' in sentence

# print(query)


sentence = 'The quick brown fox jumped over the lazy dog'

sentence = sentence.replace('quick', 'slow')

print(sentence.replace('quick', 'slow'))
print(sentence)

# Using a Negative Index with a Python String
sentence = 'The quick brown fox jumped over the lazy dog.'

print(sentence[-4:])

# Overview of Python's strip, lstrip, and rstrip Functions

url = 'https://google.com'

print(url.strip('https://'))

# url = url.lstrip('https://')
url = url.rstrip('.com')
# url = url.capitalize()

print(url.capitalize())

url = 'https://youtube.com,https://google.com,https://facebook.com'

list_of_url = url.split(',')

print(list_of_url.strip('https://'))

`Victor Laucas [12:07 PM]`
`You’re close. You can’t call the `.strip()` function on the list. You can only call it on a string`

# url = url.lstrip('https://')
# url = url.rstrip('.com')
# url = url.capitalize()

# print(url.capitalize())

solution

starter = "https://youtube.com,https://google.com,https://facebook.com"
starter_list = starter.split(",")
for item in starter_list:
  url = item.lstrip("https://")
  title = url.rstrip(".com")
  final = title.capitalize()
  print(final)

# youtube_com = starter_list[0].lstrip("https://") 
# google_com = starter_list[1].lstrip("https://")
# facebook_com = starter_list[2].lstrip("https://")

# youtube = youtube_com.rstrip(".com")
# google = google_com.rstrip(".com")
# facebook = facebook_com.rstrip(".com")

# final_youtube = youtube.capitalize()
# final_google = google.capitalize()
# final_facebook = facebook.capitalize()

# print(final_youtube)
# print(final_google)
# print(final_facebook)