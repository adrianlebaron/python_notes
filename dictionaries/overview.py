players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "DH": "Gattis",
  "OF": "Springer"
}
short_stop = players['ss']
second_base = players['2b']
third_base = players['3b']
designated_hitter = players['DH']
out_fielder = players['OF']

print(players),
print(players),
print(players),
print(players),
print(players),

# Guide to Nested Collections in Python Dictionaries
# {} means dictionary
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

astros = teams['astros']
print(astros)
print(teams['angels'])
print(teams['yankees'])

# How to Add New Key/Value Pairs to Python Dictionaries

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],# the key astros is a string and could be anything but be smart about it
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

teams['red sox'] = ['Price', 'Betts']

print(teams)