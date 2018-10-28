class Stack:
	
	def __init__(self, Size=10):
		self._size = Size
		self._stack=[]
		self._i=-1
	
	def isEmpty(self): return len(self._stack) == 0
	def isFull(self): return len(self._stack) == self._size
	
	def Push(self, value):
		if(self.isFull()): raise IndexError("Overflow Error - Stack is Full")
		else: self._stack.append(value)
	
	def Pop(self):
		if(self.isEmpty()): raise IndexError("Unerflow Error - Stack is Empty")
		return self._stack.pop()
		
	def Top(self):
		if(self.isEmpty()): raise IndexError("Stack is Empty")
		return self._stack[-1]
	
	def __len__(self):return len(self._stack)
		
	def __getitem__(self, index): return self._stack[index]
		
	def __next__(self):
		self._i+=1 
		if(self._i < self.__len__()): return self.__getitem__(self._i)
		else: raise StopIteration()
		
	def __iter__(self):
		self._i=-1
		return self
		
def Push(S1):
	if(S1.isFull()): print("\n\tOverflow Error - Stack is Full")
	else: S1.Push(input("\n\tEnter value to push in stack = "))
	
def Pop(S1):
	try: print("\n\tPopped Value = ", S1.Pop())
	except IndexError: print("\n\tUnerflow Error - Stack is Empty")
	
def See_Top(S1):
	try: print("\n\tTop Value = ", S1.Top())
	except IndexError: print("\n\tStack is Empty")
	
def Display(S1):
	print("\n\tStack : ", end='')
	for each in S1: print(each, end=', ')
		
if __name__ == '__main__':
	try: Size = int(input("\n\tEnter size of stack = "))
	except ValueError: Size=5
	
	S1 = Stack(Size)
	while 1:
		print("\n\t1. Push\n\t2. Pop\n\t3. See Top\n\t4. Display Stack\n\t5. Length of Stack\n\t6. Exit")
		try: ch = int(input("\tEnter your choice = "))
		except ValueError: ch=0
		
		if(ch==1): Push(S1)
		elif(ch==2): Pop(S1)
		elif(ch==3): See_Top(S1)
		elif(ch==4): Display(S1)
		elif(ch==5): print("\n\tLength = ", len(S1))
		elif(ch==6): break
		else: print("\n\tInvalid Input ")
		input("\n\tPress Enter to continue...")
