from timeit import timeit

Recursive = timeit("""
def Cut_Rod(Prices, n):
	if n==0: return 0
	q=-1
	for i in range(0, n):
		q = max(q, Prices[i]+Cut_Rod(Prices, n-1-i)) 
	return q
	
Prices = [1,5,8,9,10,17,17,20,24,30]
print(Cut_Rod(Prices, 10))
""", number=1)
print("Recursive = ", Recursive)


Dynamic = timeit("""
Store = {0:(0,0)}

def Cut_Rod_Memoized(Prices, n):
	try: return Store[n]
	except KeyError: pass
	
	Max_Value = Max_Len = -1
	for i in range(1, n+1):
		Current = Prices[i-1] + Cut_Rod_Memoized(Prices, n-i)[0]
		Max_Value, Max_Len = (Current, i) if(Current > Max_Value) else (Max_Value, Max_Len)
	Store[n] = (Max_Value, Max_Len)
	return Store[n]
	
Prices = [1,5,8,9,10,17,17,20,24,30]
print(Cut_Rod_Memoized(Prices, 10))
""", number=1)
print("  Dynamic = ", Dynamic)
