def gcd_divison(a, b):
    while b != 0:
        remainder = a % b
        print (f"{a} = {a//b} * {b} + {remainder}")
        a = b
        b = remainder
    return a

a = 120
b = 25

print("The Euclidean algorithm using divison:\n")
print(f"The GCD of {a} and {b} is: {gcd_divison(a, b)}")