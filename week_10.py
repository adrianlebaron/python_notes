# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="myusername",
#   passwd="mypassword"
# )

# print(mydb)

data =[
{ "Google": ["test@test.com 123", "test@test.com 321", "test@test.com 451", "test@test.com 123" ]},
{ "Yahoo": ["test@test.com 123", "test@test.com 321", "test@test.com 451", "test@test.com 451" ]},
{ "IBM": ["test@test.com 888", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
{ "GREGS": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
{ "AUTO SHOP": ["test@test.com 888", "test@test.com 555", "test@test.com 555", "test@test.com 123" ]},
{ "PAWN SHOP": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Nike": ["test@test.com 123", "test@test.com 123", "test@test.com 555", "test@test.com 123" ]},
{ "Franks": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]},
{ "Tims": ["test@test.com 123", "test@test.com 123", "test@test.com 888", "test@test.com 123" ]},
{ "Apple": ["test@test.com 123", "test@test.com 555", "test@test.com 123", "test@test.com 123" ]},
{ "Sony": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Disney": ["test@test.com 123", "test@test.com 888", "test@test.com 123", "test@test.com 123" ]},
{ "Popies": ["test@test.com 123", "test@test.com 123", "test@test.com 123", "test@test.com 123" ]},
{ "Sally": ["test@test.com 123", "test@test.com 555", "test@test.com 888", "test@test.com 123" ]},
{ "Henry": ["test@test.com 123", "test@test.com 555", "test@test.com 555", "test@test.com 555" ]},
{ "Dave's": ["test@test.com 123", "test@test.com 888", "test@test.com 555", "test@test.com 123" ]}
],
newlist = sorted(data) 

print(newlist[0])

def email_formatter(data):
  for group in data:
    for company in group:
      departments = []
      for email in group[company]:
        departments.append(email[-3:])
      print(f"""{company} - 
      {departments.count('123')}:123
      {departments.count('321')}:321
      {departments.count('451')}:451
      {departments.count('555')}:555
      {departments.count('888')}:888
      """)