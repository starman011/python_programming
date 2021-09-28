#prgram to write the factorial of a number to a string.
#n! = 1 x 2 x 3 ... n
#this program is without using def
n = 0
product = 1
for i in range(n):
    product = product * (i +1)
print(product)

#program to find factorial with def
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product *(i +1)
    return product
f = factorial_iter(5)
print(f)

#program that uses recursion
def factorial_recursive(n):
    if n == 1 or n == 0: 
        return 1
    return n*factorial_recursive(n-1)

f = factorial_recursive(5)
print(f)
