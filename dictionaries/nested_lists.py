# Guide to Working with Lists of Nested Dictionaries

teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

# print(teams[0])

angels = teams[1].get('angels', 'Team not found')

print(list(angels.values())[1])


Jobs = [
  {
    'savage :{
      'Enrique' 
        'hangers':('Manuel''Jose')
        'cleaners' : ('Mirna''Roberto')       
      }

    }
  }
    {
    'sugarmont :{
      'Eleazar':
      { 'hangers':('armando''jesus')
        'framer':'Zacharias'
      }

    }
  }
]
