#!/usr/bin/python3.4

"""
    Reads text files and lets the user add their own text anywhere
    the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
"""
filler = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
answer = []
#text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

file = open('/home/razvan/python/sentence.txt', 'r')
content = file.read().split()

for word in content:
    if word.strip('.|!|?|,') in filler:
        answer.append(input('Enter a {0}: '.format(word)))
    else:
        answer.append(word)

file = open('/home/razvan/python/sentence.txt', 'w')
file.write(' '.join(answer))
file.close()
