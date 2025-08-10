def knapsack_brute_force(capacity, n):
    print(f'knapsack_brute_force({capacity}, {n})')
    if n == 0 or capacity == 0:
        return 0
    
    elif weights[n - 1] > capacity:
        return knapsack_brute_force(capacity, n - 1)

    else:
        include_item = values[n - 1] + knapsack_brute_force(capacity - weights[n - 1], n - 1)
        exclude_item = knapsack_brute_force(capacity, n - 1)
        return max(include_item, exclude_item)

values = [300, 200, 400, 500]
weights = [2, 1, 5, 3]
capacity = 10
n = len(values)

print('\nMaximum value in Knapsack =', knapsack_brute_force(capacity, n))