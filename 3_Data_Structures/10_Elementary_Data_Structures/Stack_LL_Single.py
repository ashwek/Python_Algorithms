class Node:
	def __init__(self, Value, Next=None):
		self.__value = Value
		self.__next = Next

	def get_value(self): return self.__value
	def get_next(self): return self.__next
	
class LL_Single:
	def __init__(self):
		self._top = None
		self._len = 0
		
	def isEmpty(self): return self._top==None
	
	def Push(self, data):
		self._top = Node(data, self._top)
		self._len+=1
	
	def Pop(self):
		if(self.isEmpty()): raise IndexError("Stack is Empty")
		else:
			temp = self._top
			self._top = self._top.get_next()
			self._len-=1
			return temp.get_value()
			
	def __len__(self): return self._len
	
	def Elements(self):
		if(self.isEmpty()): raise StopIteration("Stack is Empty")
		else:
			temp = self._top
			while(temp != None): 
				yield temp.get_value()
				temp=temp.get_next()
			
def Push(S_LL1): S_LL1.Push(input("\n\tEnter a value = "))

def Pop(S_LL1):
	if(S_LL1.isEmpty()): print("\n\tStack Empty")
	else: print("\n\tPopped value = ", S_LL1.Pop())

def Display(S_LL1):
	print("\n\tStack : (", end='')
	for each in S_LL1.Elements(): print(each, end=', ')
	print(')')

if __name__ == '__main__':
	S_LL1 = LL_Single()
	while 1:
		print("\n\t1. Push\n\t2. Pop\n\t3. Display Stack\n\t4. Length of Stack\n\t5. Exit")
		try: ch = int(input("\tEnter your choice = "))
		except ValueError: ch=0
		
		if(ch==1): Push(S_LL1)
		elif(ch==2): Pop(S_LL1)
		elif(ch==3): Display(S_LL1)
		elif(ch==4): print("\n\tLength = ", len(S_LL1))
		elif(ch==5): break
		else: print("\n\tInvalid Input ")
		input("\n\tPress Enter to continue...")
		
