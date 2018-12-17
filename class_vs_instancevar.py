# Class vs Instance Attributes in Python video

class Website:
  title = 'My site title'


ws = Website()
ws.title = 'Updated title'
print(ws.__dict__)

class SecondWebsite:
  def __init__(self, title):
    self.title = title


second_ws = SecondWebsite('Another Title')
print(second_ws.__dict__)

class Website:
  title = 'My site title'


print(Website.title)