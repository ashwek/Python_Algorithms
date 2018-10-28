def Counting_Sort(A, d, Digit):
	C = [0]*10
	for x in A: C[int(str(x).rjust(Digit, '0')[d])]+=1
	for x in range(1, 10): C[x]+=C[x-1]
	B=list(range(len(A)))
	for i in range(len(A)-1, -1, -1):
		x = A[i]
		B[C[int(str(x).rjust(Digit, '0')[d])]-1]=x
		C[int(str(x).rjust(Digit, '0')[d])]-=1
	return B

def Radix_Sort(A, Digit):
	for d in range(Digit-1, -1, -1):
		A=Counting_Sort(A, d, Digit)
	return A
A = [329,457,657,839,436,720,355]
A=Radix_Sort(A, 3)
print(A)
