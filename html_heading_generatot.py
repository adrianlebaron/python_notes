# Build an HTML Heading Generator Function in Python

"""
heading_generator(title, title, heading_type)
heading_generator('Greeting', '1')
<h1>Greeting</h1>

heading_generator('Hi there', '3')
<h3>Hi there</h3>
"""

# `two ways to do something below return or print`
def heading_generator(title, heading_type):
    print(f'<h{heading_type}>{title}</h{heading_type}>')  #f means string interpolation

def heading_generator(title, heading_type):
    return f'<h{heading_type}>{title}</h{heading_type}>'    
print(heading_generator('hello there', '3'))


