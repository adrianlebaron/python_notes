teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels" :  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

print(teams.get('mets', 'No team found by that name'))

teams.pop('astros', 'No team found by that name')
teams.pop('astros', 'No team found by that name')

del teams['angels']
removed_team = teams.pop('mets', 'Team not found') #can pass in a string in a dictionary content

print(teams)
print(removed_team)
