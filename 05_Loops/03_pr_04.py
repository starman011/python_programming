#program to find wheather a number is prime or not
l1 = int(input("Write the number: \n"))
prime = True
for i in range(2,l1):
    if(l1%i == 0):
        prime = False
        break
if prime:
    print("This is prime")
else:
    print("This number is not prime")

