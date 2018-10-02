# This program says hello and asks for my name

print('Hello world!')

print('What is your name?')    # ask for their name
myname = input()
print('It is good to meet you, ' + myname)
print('The lenght of your name is:')
print(len(myname))

print('What is your age?')     # Ask for their age
myage = input()
print('You will be ' + str(int(myage) + 1) + ' in a year.')
