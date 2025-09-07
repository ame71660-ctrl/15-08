import string
import keyword
name = input("Введіть рядок: ")
if not name:
    print(False)
elif name == "_":
    print(True)
elif set(name) == {"_"} and len(name)>1:
    print(False)
elif name[0].isdigit():
    print(False)
elif any(ch.isdigit() for ch in name) or any(ch in string.punctuation and ch != "_" for ch in name):
    print(False)
elif name in keyword.kwlist:
    print (False)
else:
    print(True)