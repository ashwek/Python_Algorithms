def Insertion_Sort(A):
	for i in range(1, len(A)):
		key = A[i]
		j=i-1
		while(j>=0 and A[j]>key):
			A[j+1] = A[j]
			j-=1
		A[j+1] = key
		
A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(A)
Insertion_Sort(A)
print(A)
