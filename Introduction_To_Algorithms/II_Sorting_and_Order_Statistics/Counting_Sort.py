def Counting_Sort(A, k=-1):
	if(k==-1): k=max(A)
	C = [0 for x in range(k+1)]
	for x in A: C[x]+=1
	for x in range(1, k+1):C[x]+=C[x-1]
	B = [0 for x in range(len(A))]
	for i in range(len(A)-1, -1, -1):
		x = A[i]
		B[C[x]-1] = x
		C[x]-=1
	return B
		
A = [13,20,18,20,12,15,7]
print(Counting_Sort(A))
