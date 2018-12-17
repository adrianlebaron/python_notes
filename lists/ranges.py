tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[2:]
tag_range = tags[0:2]
tag_range = tags[:2]
tag_range = tags[0:-1]

print(tag_range)

# Advanced Techniques for Implementing Ranges and Slices in Python Lists video

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[1:-1:2]
tag_range = tags[::-1] #this reverses this list not the same as .sort(reverse=True)

print(tag_range)

tags.sort(reverse=True)#cannot store this in avariable

print(tags)

my_range = range(1,200)
print 10 * x in my_range

print(list(map(str my_range)))