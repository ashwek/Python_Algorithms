from heapq import heappush
from heapq import heappop

def Build_Min_Heap(A):
	H = []
	for each in A: heappush(H, each)
	return H
	
def Ascending_Heap_Sort(A):
	H = Build_Min_Heap(A)
	K=0
	while(len(H)>0):
		A[K] = heappop(H)
		K+=1
			
A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print("   Orignal Array = ", A)
Ascending_Heap_Sort(A)
print("Descending Order = ", A)
