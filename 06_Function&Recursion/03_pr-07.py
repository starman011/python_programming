#program to remove a word from a list and strip at the same time
a = "     Earth is: round     "

def remove_strip(a):
    b = a.replace("is","")
    return(b.strip())

c = remove_strip(a)
print(c)


