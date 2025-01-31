#ask user for input of seq
askUser = int(input('Enter the sequence to print: '))

#print seq 1 and 2, and get a count of numbers printed
print(0)
print(1)
count = 2

# define the fibonacci function
def fib(prev1, prev2):
    global count
    if count <= askUser:
        newFib = prev1 + prev2
        print (newFib)
        prev2 = prev1
        prev1 = newFib
        count += 1
        fib(prev1, prev2)

    else:
        return
    
fib(0, 1)