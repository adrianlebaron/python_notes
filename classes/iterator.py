# How to Build a Custom Iterator Class in Python video

class Lineup:

    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):
        self.n = 0
        return self

    def get_player(self, n):
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index:
            self.n += 1
            return self.get_player(self.n)
        elif self.n == self.last_player_index:
            self.n = 0
            return self.get_player(self.n)


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))