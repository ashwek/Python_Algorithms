from random import random
from math import floor

def Max_Min(A):
	Max = Min = A[0]
	A.append(A[-1])
	for i in range(1, len(A)-1, 2):
		t_min, t_max = (A[i], A[i+1]) if A[i]<A[i+1] else (A[i+1], A[i])
		Max = t_max if t_max>Max else Max
		Min = t_min if t_min<Min else Min
	return (Max, Min)
			
A = [floor(random()*100) for x in range(50)]
print(Max_Min(A))
