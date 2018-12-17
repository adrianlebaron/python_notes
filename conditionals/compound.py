# How to Build Compound Conditionals in Python video


username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth': 
  print('Access permitted')
else:
  print('Not allowed')


if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if username == 'jonsnow' or password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standard dashboard')

at_school = True
goofing_off = False
if at_school and not goofing_off:
  print('you are hired' )
else:
  print('you are dum')

at_school = True
goofing_off = False
if at_school and goofing_off:
  print('you are hired' )
else:
  print('you are dum')

at_school = True
goofing_off = False
if at_school or goofing_off:
  print('you are hired' )
else:
  print('you are dum')