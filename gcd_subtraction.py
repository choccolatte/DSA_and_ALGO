def gcd_subtraction(a, b):
    while a != b:
        if a > b:
            print(f"{a} - {b} = {a-b}")
            a = a - b
        else:
            print(f"{b} - {a} = {b-a}")
            b = b - a
    return a

a = 120
b = 25
print("The Euclidean algorithm using subtraction:\n")
print(f"The GCD of {a} and {b} is: {gcd_subtraction(a, b)}")
