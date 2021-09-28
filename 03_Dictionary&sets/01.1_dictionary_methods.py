#dictionary methods
myDict = {
    "parrot": "a fat bird",
    "reptile": "crawling creature",
    "mar": [1,23,4,2],
    }
#dictionary methods
print(myDict.keys()) #01print the keys
print(myDict.values()) #02print the values
print(myDict.items()) #03print the key and value 

#04can convert all these to list
# print(list(myDict.keys()) #print the keys

#05updating the dictionary
print(myDict)
updateDict = {
    "hi": "symbolises meet",
    "bye":"going afk"
}
myDict.update(updateDict) #update the dictionary
print(myDict)
#searching for keywords using get
print(myDict.get("parrot"))
