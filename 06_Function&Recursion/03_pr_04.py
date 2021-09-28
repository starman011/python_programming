#program to calculate the sum of n natural numbers using recrsion
#sum = sum(n-1)+n
a = int(input("Write the number\n"))

def ad_recursion(a):
    if a ==1 :
        return 1
    elif a == 0:
        return 0
    else:
        return a +ad_recursion(a-1)

b = ad_recursion(a)   
print("The sum of n natural numbers are:\n",b)
