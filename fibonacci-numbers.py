# take the first two numbers

prevNo = 0
nextNo = 1

# ask how many numbers user wants to print

noOfSeq = int(input('Enter no. of Fibonacci sequence to print: '))

# print them for 1st and 2nd sequence

print(prevNo)
print(nextNo)

# loop through range of numbers you want to print

for fib in range(noOfSeq):
    newNo = prevNo + nextNo
    prevNo = nextNo
    nextNo = newNo
    print(nextNo)


