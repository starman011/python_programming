#detecting spam messages
comment = input("Write the spam message")

if("make a  lot of money" in comment):
    spam = True
if("but now" in comment):
    spam = True
if("click this" in comment):
    spam = True
if("subscribe this" in comment):
    spam = True
else:
    spam = False

if(spam is True):
    print("This text is spam")
else:
    print("this is not a spam")

    

    