#program to detect name in any indentation
a = input("Write the name you want to search:\n")
b = ["Shyam","SHYAM","ShyaM","SHyam","SHYam","SHYAm","SHYAM","shyam"]
if (a in b):
    print("YES Detected")
else:
    print("NO")
    