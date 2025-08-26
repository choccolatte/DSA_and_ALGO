computation_count = 0
def F(n):
    global computation_count
    computation_count += 1
	
	if n <= 1:
		return n
	else:
		return F(n - 1) + F(n - 2)

computation_count_mem = 0
def F_mem(n):
    if memo[n] != None: #alredy computed
        return memo[n]
    else: #computation needed
        global computation_count_mem
        computation_count_mem += 1
        print('Computing F('+str(n)+')')

        if n <= 1:
            return n
        else:
            return F(n - 1) + F(n - 2)
        return memo[n]
    
print('F(30) = ', F(30))
print(f'Number of computations: {computation_count}')
print('\nUsing memoization:')

memo = [None] * 31

print('F(30) = ',F_mem(30))
print(f'Number of computations with memoization: {computation_count_mem}')