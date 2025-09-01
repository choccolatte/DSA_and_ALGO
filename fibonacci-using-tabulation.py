def fib_tabulation(n):
    if n == 0: return 0
    elif n == 1: return 1

    F = [0] * (n + 1)
    F[0] = 0
    F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]

    print(F)
    return F[n]

n = 10
result = fib_tabulation(n)
print(f'\nThe {n}th Fibonacci number is {result}')