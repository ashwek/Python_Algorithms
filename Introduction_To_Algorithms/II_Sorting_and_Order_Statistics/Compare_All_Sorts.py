from timeit import timeit

Print_Size=18
print("\tTime taken to sort 900-0 in Ascending Order")

Counting = timeit("""
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
		
A = list(range(900,0,-1))
Counting_Sort(A)
""", number=1)
print("Counting Sort =".rjust(Print_Size), Counting, "seconds")

Heap = timeit("""
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
		
A = list(range(900,0,-1))
Ascending_Heap_Sort(A)
""", number=1)
print("Heap Sort =".rjust(Print_Size), Heap, "seconds")

Merge = timeit("""
from math import floor

def Merge(A, start, mid, end):
	Left, Right = A[start:mid], A[mid:end]
	Max = max(Left[-1], Right[-1])+1
	Left.append(Max)
	Right.append(Max)
	i = j = 0
	for count in range(start, end):
		if(Left[i] < Right[j]):
			A[count] = Left[i]
			i+=1
		else:
			A[count] = Right[j]
			j+=1
		
def Merge_Sort(A, start, end):
	if(start < end-1):
		mid = floor((start+end)/2)
		Merge_Sort(A, start, mid)
		Merge_Sort(A, mid, end)
		Merge(A, start, mid, end)
	
A = list(range(900,0,-1))
Merge_Sort(A, 0, len(A))
""", number=1)
print("Merge Sort =".rjust(Print_Size), Merge, "seconds")

Radix = timeit("""
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
A = list(range(900,0,-1))
A=Radix_Sort(A, 3)
""", number=1)
print("Radix Sort =".rjust(Print_Size), Radix, "seconds")

Quick = timeit("""
def Partition(A, low, high):
	Pivot = A[high-1]
	i = low-1
	for j in range(low, high-1):
		if(A[j] < Pivot):
			i+=1
			A[i], A[j] = A[j], A[i]
	A[i+1], A[high-1] = A[high-1], A[i+1]
	return i+1

def Quick_Sort(A, low, high):
	if(high-low > 1):
		mid = Partition(A, low, high)
		Quick_Sort(A, low, mid)
		Quick_Sort(A, mid+1, high)
		
A = list(range(900,0,-1))
Quick_Sort(A, 0, len(A))
""", number=1)
print("Quick Sort =".rjust(Print_Size), Quick, "seconds")

Insertion = timeit("""
def Insertion_Sort(A):
	for i in range(1, len(A)):
		key = A[i]
		j=i-1
		while(j>=0 and A[j]>key):
			A[j+1] = A[j]
			j-=1
		A[j+1] = key
		
A = list(range(900,0,-1))
Insertion_Sort(A)
""", number=1)
print("Insertion Sort =".rjust(Print_Size), Insertion, "seconds")

Bubble = timeit("""
def Bubble_Sort(A):
	for i in range(len(A)):
		for j in range(len(A)-1):
			if(A[j] > A[j+1]): A[j], A[j+1] = A[j+1], A[j]
		
A = list(range(900,0,-1))
Bubble_Sort(A)
""", number=1)
print("Bubble Sort =".rjust(Print_Size), Bubble, "seconds")
