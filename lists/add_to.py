tags = ['python', 'development', 'tutorials', 'code']

# Nope
tags[-1] = 'Programming' #replaces

# In Place
tags.extend('Programming') #adds every integer as its own charachter hardly  used
tags.extend(['Programming']) #if you do not want the above add the brackets not able to be a variable

# New List
new_tags = tags + ['Programming']  #adds on and makes new variable need brackets

print(new_tags)

print(tags)