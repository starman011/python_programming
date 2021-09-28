#create a dictionary of hindi words with values as their english translation
myDict = {
    "balla":"bat",
    "pankha":"fan"
}
print("options are:",myDict.keys())
a = input("write the hindi word\n")
print("the meaning of the word is:",myDict.get(a))#here at the last myDict[a] is used this is  to call the input variable that is entered ,so that it can fetch that data

