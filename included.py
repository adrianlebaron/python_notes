# How to Check if a Value is Included in a Python String or List video

sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'dog'

if word.lower() in sentence.lower(): ## .lower is a function so it needs () without the function you would not need the parenthesis
  print('The word is in the sentence')
else:
  print('The word is not in the sentence')


nums = [1, 2, 3, 4]

if 3 in nums:
  print('The number was found')
else:
  print('The number was not found')