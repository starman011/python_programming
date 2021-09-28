greeting = 'Good Morning,'
name = 'Saqlain'

y = greeting + name
print(y[2])#this [] is used to call index in a particular string
print(y[0:8])#print from 0 to 8
print(y[:8])#will print the same as[0:8]
print(y[0:])#will print the same as [0:19]
print(y[-1])#print the last string 

#slicing with skip value
print(y[0:13:3])#this last digit means that it will print every 3rd character

#advance slicing techniques
print(y[:7])
print(y[0:])
