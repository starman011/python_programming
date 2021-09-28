#printing a multiplication table in reverse order


b = int(input("Write the number\n"))

for i in range(1,11,):
    # print(str(b), "X" , str(i),"=" ,i * b)
  
# or we can use f string to make it easier
    print(f"{b}X{i}={b*i}")#this command takes function inside curly bracket
r = b*i
l1 = [r[1]]
print(l1)
