import re

message = 'Call me 415-555-1011 tommorow, or at 115-555-1234 for my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message))
