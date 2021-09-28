# taking out factorial of a given number 
l1 = int(input("Write the number"))

factorial = 1
for i in range(1,l1+1):
    factorial = factorial * i
print(f"The factorial of the {l1} is :{factorial}")
     
    
