def knapsack_brute_force(capacity, n):
    print(f'knapsack_brute_force({capacity}, {n})')

    if memo[n][capacity] is not None:
        print(f'Using memo for({n}, {capacity})')
        return memo[n][capacity]

    if n == 0 or capacity == 0:
        return 0
    
    elif weights[n - 1] > capacity:
        return knapsack_brute_force(capacity, n - 1)

    else:
        include_item = values[n - 1] + knapsack_brute_force(capacity - weights[n - 1], n - 1)
        exclude_item = knapsack_brute_force(capacity, n - 1)
        return max(include_item, exclude_item)

    memo[n][capacity] = result
    return result

values = [300, 200, 400, 500]
weights = [2, 1, 5, 3]
capacity = 10
n = len(values)

memo = [[None] * (capacity + 1) for _ in range(n + 1)]

print('\nMaximum value in Knapsack =', knapsack_brute_force(capacity, n))