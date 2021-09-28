#program to find sum of first n natural numbers.
num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum = sum + num  
       num = num - 1 
   print("The sum is",sum)  