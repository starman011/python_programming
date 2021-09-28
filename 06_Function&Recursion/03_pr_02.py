#convert celcius to farenheit
Celcius = int(input("Write the degree in Celcius\n"))

def temp():
    Farenheit = Celcius  * (9/5)+32
    return(Farenheit)

b = temp()
print("The Degreee in Farenheit is : ",b)

