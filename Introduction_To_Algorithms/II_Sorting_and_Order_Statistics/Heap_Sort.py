from math import floor

Parent = lambda i: floor(i/2-0.5)
Child = lambda i, s=1: (2*i)+s

def Max_Heapify(A, i, Len=-1):
	if(Len == -1): Len = len(A)
	L, R = Child(i), Child(i, 2)
	
	if(L<Len and A[L]>A[i]): largest = L
	else: largest = i
	if(R<Len and A[R]>A[largest]): largest = R
	if(largest != i): 
		A[i], A[largest] = A[largest], A[i]
		Max_Heapify(A, largest, Len)
	
def Build_Max_Heap(A):
	for i in range(floor(len(A)/2), -1, -1): Max_Heapify(A, i)
		
def Ascending_Heap_Sort(A):
	Build_Max_Heap(A)
	for x in range(len(A)-1, -1, -1):
		A[0], A[x] = A[x], A[0]
		Max_Heapify(A, 0, x)

def Min_Heapify(A, i, Len=-1):
	if(Len == -1): Len = len(A)
	L = Child(i)
	R = Child(i, 2)
	
	if(L<Len and A[L]<A[i]): least = L
	else: least = i
	if(R<Len and A[R]<A[least]): least = R
	if(least != i): 
		A[i], A[least] = A[least], A[i]
		Min_Heapify(A, least, Len)
	
def Build_Min_Heap(A):
	for i in range(floor(len(A)/2), -1, -1): Min_Heapify(A, i)
		
def Descending_Heap_Sort(A):
	Build_Min_Heap(A)
	for x in range(len(A)-1, -1, -1):
		A[0], A[x] = A[x], A[0]
		Min_Heapify(A, 0, x)		
		
A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print("   Orignal Array = ", A)
Ascending_Heap_Sort(A)
print(" Ascending Order = ", A)
Descending_Heap_Sort(A)
print("Descending Order = ", A)
