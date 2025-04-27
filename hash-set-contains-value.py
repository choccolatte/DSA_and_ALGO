myHashNewSet = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def hashFunction(value):
    return sum(ord(char) for char in value) % 10

def add(value):
    index = hashFunction(value)
    bucket = myHashNewSet[index]
    if value not in bucket:
        bucket.append(value)

def contains(value):
    index = hashFunction(value)
    bucket = myHashNewSet[index]
    return value in bucket

add('Stuart')

print(myHashNewSet)
print('Contains Stuart: ', contains('Stuart'))