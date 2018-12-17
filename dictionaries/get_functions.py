# Guide to Using the get Function in Python Dictionaries to Configure Fallback Lookup Values

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}

featured_team = teams.get('yankees', 'No featured team')
featured_team = teams.get('mets', 'No featured team') # if cannot find will return 

featured_team = teams.get('yankees', 'No featured team')
print(featured_team)