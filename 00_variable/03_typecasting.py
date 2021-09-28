# shows type casting and type function
a = "132"
print(type(a))
print(a+3)
# this will show error cause a is a string 

# now we solve this by using typecasting
a = "132"
a = int(a)
print(type(a))
print(a+3)