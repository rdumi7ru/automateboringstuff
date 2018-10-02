import pprint, operator
message = 'It was a bright day in April, and the clocks were striking thirteen'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

key_max = max(count.keys(), key=(lambda k: count[k]))
key_min = min(count.keys(), key=(lambda k: count[k]))
#text = pprint.pformat(count)
print('Maximum Value: ',count[key_max])
print('Minimum Value: ' + str(count[key_min]))
#print(text)
