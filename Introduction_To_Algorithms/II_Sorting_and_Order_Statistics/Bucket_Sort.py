def Bucket_Sort(A, Digit):
	B = [[] for x in range(10)]
	for each in A: 
		B[int(str(each).rjust(Digit, '0')[0])].append(each)
	for each in range(10):B[each].sort()
	A=[]
	for bucket in B:
		for each in bucket:
			A.append(each)
	return A
	
A = list(range(50,0,-1))
A=Bucket_Sort(A, 2)
print(A)
