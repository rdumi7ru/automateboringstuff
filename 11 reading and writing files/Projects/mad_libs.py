#!/usr/bin/python3.4

import re

madText = open('/home/razvan/python/madText.txt', 'w')
text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

madText.write(text)
madText.close()

content = re.split('\W+', text)
# output = []

for i in content:
    if i == 'ADJECTIVE':
        replace_regex = re.compile(r'(ADJECTIVE)')
        adjective = input(('Please enter an Adjective\n'))
        output = replace_regex.sub(adjective, str(content))
    
    elif i == 'NOUN':
        replace_regex = re.compile(r'NOUN')
        noun = input(('Please enter a Noun\n'))
        output = replace_regex(noun, str(content))

    elif i == 'VERB':
        replace_regex = re.compile(r'(')

