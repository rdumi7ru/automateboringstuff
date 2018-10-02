print ('How many cats do you have?')
numCats = input()

try:
    if int(numCats) < 0:
        print ('Sorry the number must be a positive number')
    
    elif int(numCats) >= 4:
        print ('That is a lot of cats.')
    else:
        print ('That is not that many cats.')
except ValueError:
    print ('You did not entered a number')