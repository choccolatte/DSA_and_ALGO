def F(n):
    if memo[n] != None: #alredy computed
        return memo[n]
    else:
        print('Computing F('+str(n)+')')
        if n <= 1:
            return n
        else:
            return F(n - 1) + F(n - 2)
        return memo[n]
    
memo = [None] * 7
print('F(6) = ',F(6))
print('memo = ', memo)