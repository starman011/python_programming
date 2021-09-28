a = input("Write the name\n")
b = input("Write the date\n")

letter = '''Dear <|NAME|>
greetings !!
             you are selected!
             <|DATE|>'''
letter=letter.replace("<|NAME|>",a)
letter=letter.replace("<|DATE|>",b)

print(letter)



