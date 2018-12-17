players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

print(players.keys())
print(players.values()) #cannot treat as list cannot use values or ranges
print(players.items()) # don not forget to use the key function

player_names = list(players.copy().values())#remember to addd a list.

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels" :  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()

"""
[
  ('astros', ['Altuve', 'Correa', 'Bregman']),
  ('angels', ['Trout', 'Pujols']),
  ('yankees', ['Judge', 'Stanton']),
  ('red sox', ['Price', 'Betts'])
]
"""

print(list(team_groupings)[1][1][0])

# https://docs.python.org/3.0/library/stdtypes.html#dictionary-view-objects