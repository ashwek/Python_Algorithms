def Print_Optimal(S, i, j):
	if(i==j): print("A", i, sep="", end="")
	else:
		print("(", end="")
		Print_Optimal(S, i, S[i][j])
		Print_Optimal(S, S[i][j]+1, j)
		print(")", end="")
		
	
def Matrix_Chain_Order(D):
	N = len(D)-1
	M = [[-1]*(N+1) for x in range(N+1)]
	S = [[0]*(N+1) for x in range(N+1)]
	
	for i in range(N, 0, -1):
		for j in range(i, N+1):
			if(i == j): M[i][j] = 0
			else:
				for k in range(i, j):
					q = M[i][k] + M[k+1][j] + (D[i-1]*D[k]*D[j])
					if(M[i][j]==-1 or q<M[i][j]): M[i][j], S[i][j] = q, k
	
	Print_Optimal(S, 1, N)

Dimensions = [30,35,15,5,10,20,25]
Matrix_Chain_Order(Dimensions)
