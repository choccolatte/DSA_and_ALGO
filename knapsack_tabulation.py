def knapsack_tabulation():
    n = len(values)
    tab = [[0] * (capacity + 1) for y in range(n + 1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= 2:
                include_item = values[i-1] + tab[i-1][w-weights[i-1]]
                exclude_item = tab[i-1][w]
                tab[i][w] = max(include_item, exclude_item)
            else:
                tab[i][w] = tab[i-1][w]

    for row in tab:
        print(row)
    return tab[n][capacity]

values = [300, 200, 400, 500]
weights = [2, 1, 5, 3]
capacity = 10
print('\nMaximum value in Knapsack = ', knapsack_tabulation())
