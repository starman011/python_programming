b = set()
print(type(b))

#to add something to the sets
b.add(2)
b.add(5)
b.add(5)#repitition are ignored
b.add((1,32))#tuples are being added 
print(b)

#shows the length of sets
print(len(b))
#removes the item
b.remove(2)#removes 2
print(b)

#pops up a random value
b.pop()
print(b)

#clear the list
b.clear()
print(b)


