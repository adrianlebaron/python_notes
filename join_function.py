# Using the join Function in Python to Build a URL Query String

# https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'

print(query_uri)

# https://www.google.com/search?q=python+development+tutorial
def search_results(list_of_searches):
  uri = 'https://www.google.com/search?q='
  # tags = ['python', 'development', 'tutorial']
  tags = list_of_searches
  formatted_tags = '+'.join(tags)
  query_uri = f'{uri}{formatted_tags}'
  print(query_uri)

search_results(['Northface', 'coat', "large"])