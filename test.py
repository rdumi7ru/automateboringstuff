import shelve

key = input(('Enter the keyword:\n'))

shelfFile = shelve.open('/home/razvan/python/filename')
shelfFile['cats'] = ['Pooka', 'Simon']
shelfFile['dogs'] = ['Ursu', 'Tookie']

print(list(shelfFile.keys()))
del shelfFile[key]

print(list(shelfFile.keys()))
shelfFile.close()
