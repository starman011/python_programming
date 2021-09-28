#converting inches to centimeters.
a = int(input("Write the value in inches\n"))

def centi_convert(a):
    b = a *2.5
    return(b)

c = centi_convert(a)
print("The value in centimeters is: ",c)
