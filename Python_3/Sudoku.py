"""
Rules:
The classic Sudoku game involves a grid of 81 squares. The grid is divided into nine blocks, each containing nine squares.

The rules of the game are simple: each of the nine blocks has to contain all the numbers 1-9 within its squares. Each number can only appear once in a row, column or box.

The difficulty lies in that each vertical nine-square column, or horizontal nine-square line across, within the larger square, must also contain the numbers 1-9, without repetition or omission.

Every puzzle has just one correct solution.


Using "Penciling In" Method from
https://www.bigfishgames.com/blog/how-to-solve-sudoku-puzzles-quickly-and-reliably/


"""

import sys, os

def Print(Sudoku):
	for x in Sudoku: print(' '.join(map(str, x)))
	print()

def Input(Sudoku):
	for x in range(9):Sudoku.append(list(map(str, input().split())))

	for r in range(9):
		for c in range(9):
			if(Sudoku[r][c] == '-'):Sudoku[r][c]=0
			else:Sudoku[r][c] = int(Sudoku[r][c])
			
def In_Nonet(Sudoku, Value, R, C):
	if(R>=0 and R<=2):R=0
	elif(R>=3 and R<=5):R=3
	else:R=6
	
	if(C>=0 and C<=2):C=0
	elif(C>=3 and C<=5):C=3
	else:C=6
	
	for row in range(R, R+3):
		for column in range(C, C+3):
			if(Value == Sudoku[row][column]):return True
	return False
	
def In_Column(Sudoku, Value, Column):
	for r in range(len(Sudoku)):
		if(Value == Sudoku[r][Column]):return True
	return False

def Remove_Repeating(Sudoku):
	for r in range(9):
		for c in range(9):
			try:
				len(Sudoku[r][c])
				each=0
				while(each<len(Sudoku[r][c])):
					if(Sudoku[r][c][each] in Sudoku[r]):
						Sudoku[r][c].remove(Sudoku[r][c][each])
						each-=1
					each+=1
				each=0
				while(each<len(Sudoku[r][c])):
					if(In_Column(Sudoku, Sudoku[r][c][each], c)): 
						Sudoku[r][c].remove(Sudoku[r][c][each]);
						each-=1
					each+=1
				each=0
				while(each<len(Sudoku[r][c])):
					if(In_Nonet(Sudoku, Sudoku[r][c][each], r, c)):
						Sudoku[r][c].remove(Sudoku[r][c][each]);
						each-=1
					each+=1
			except TypeError:pass
			except:print(sys.exc_info())
			
	
def Add_List(Sudoku):
	Lts=[1,2,3,4,5,6,7,8,9]
	for r in range(9):
		for c in range(9):
			if(Sudoku[r][c]==0): Sudoku[r][c] = list(Lts)

def Single(Sudoku):
	for r in range(9):
		for c in range(9):
			try:
				if(len(Sudoku[r][c])==1):Sudoku[r][c] = Sudoku[r][c][0]
			except:pass
	
def Solved(Sudoku):
	Scr=0
	for r in Sudoku:
		for c in r:
			try:len(c)
			except:Scr+=1
	if(Scr==81):return True
	else:return False
						
def Solve(Sudoku):
	Add_List(Sudoku)
	Remove_Repeating(Sudoku)
	while(not Solved(Sudoku)):
		Single(Sudoku)	
		Remove_Repeating(Sudoku)
			
os.system("clear")

Sudoku=[]
print("\n\tEnter Sudoku Below (use - for blank Spots): ")
Input(Sudoku)
Solve(Sudoku)
print("\nSolved:")
Print(Sudoku)

