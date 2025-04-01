myHashSet = [None,'Jones',None,'Lisa',None,'Bob',None,'Siri','Pete',None]

def hashFunc(value):
    sumOfChars = 0
    for char in value:
        sumOfChars += ord(char)

    return sumOfChars % 10

def containsValue(name):
    index = hashFunc(name)
    return myHashSet[index] == name

print("'Pete' is in Hash Set:", containsValue('Pete'))
