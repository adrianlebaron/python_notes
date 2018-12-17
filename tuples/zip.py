# Guide to Python's Zip Function video
# this is to add 2 lists together.

positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(positions, players)

print(list(scoreboard))
