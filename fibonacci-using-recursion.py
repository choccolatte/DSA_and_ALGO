def F(n):
    print('Computing F('+str(n)+')')
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)
    
print('F(6) = ',F(6))