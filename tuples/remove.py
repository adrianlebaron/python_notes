# #Three Ways to Remove Elements from a Python Tuple

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from end
post = post[:-1]

# Removing elements from beginning
post = post[1:]

# Removing specific element (messy/not recommended)
post = list(post)   ##converts to list 
post.remove('published')
post = tuple(post)   ## converts to tuple once again

print(post)