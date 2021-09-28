#program to write the multiplication table

a = int(input("Write the number\n"))

def mul_table(a):
    for i in range(1,11):
        print(f"{a} X {i} =",i*a)

mul_table(a)

    
