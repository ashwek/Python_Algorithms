from math import floor

def Max_Across(Arr, low, mid, high):
	Rht_Max = Lft_Max = min(Arr[low:high])-1
	Left, Right = low, high
	Sum = 0
	for i in range(mid-1, low-1, -1):
		Sum = Sum + Arr[i]
		if(Sum > Lft_Max): Lft_Max, Left = Sum, i
	Sum=0
	for i in range(mid, high):
		Sum = Sum + Arr[i]
		if(Sum > Rht_Max): Rht_Max, Right = Sum, i
	return (Left, Right, Lft_Max+Rht_Max)

def Max(Arr, low, high):
	if(low == high-1): return (low, high, Arr[low])
	else:
		mid = floor((low+high)/2)
		Lft_Low, Lft_High, Lft_Max = Max(Arr, low, mid)
		Rht_Low, Rht_High, Rht_Max = Max(Arr, mid, high)
		Ctr_Low, Ctr_High, Ctr_Max = Max_Across(Arr, low, mid, high)
		if(Lft_Max > Rht_Max and Lft_Max > Ctr_Max): return (Lft_Low, Lft_High, Lft_Max)
		elif(Rht_Max > Lft_Max and Rht_Max > Ctr_Max): return (Rht_Low, Rht_High, Rht_Max)
		else: return (Ctr_Low, Ctr_High, Ctr_Max)
	
A = (13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7)
print(Max(A, 0, len(A)), len(A))
