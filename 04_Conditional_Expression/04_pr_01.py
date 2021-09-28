#program to find greatest number 
n1 = int(input("Write the number"))
n2 = int(input("Write the number"))
n3 = int(input("Write the number"))
n4 = int(input("Write the number"))

if(n1>n2):
    f1 = n1
else:
    f1 = n4

if(n2>n3):
    f2 =  n2 
else: 
    f2 = n3

if(f1>f2):
    print(f1,"is greatest ")
if(f1<f2):
    print(f2,"is greatest")