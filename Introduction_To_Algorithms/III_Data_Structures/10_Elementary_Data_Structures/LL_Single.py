class Node:
	def __init__(self, Value, Next=None):
		self._value = Value
		self._next = Next
	
class LL_Single:
	def __init__(self):
		self._head = self._tail = None
		self._len=0
		
	def isEmpty(self): return self._head==None
	
	def Insert(self, Node):
		if(self._head == None): self._head = self._tail = Node
		else:
			self._tail._next = Node
			self._tail = Node
		self._len+=1
	
	def Delete(self):
		if(self.isEmpty()): raise IndexError("LL Empty")
		else:
			temp = self._head
			if(temp == self._tail): self._head = self._tail = None
			else:
				while(temp._next != self._tail): temp=temp._next
				self._tail = temp
				temp = temp._next
				self._tail._next = None
			self._len-=1
			return temp._value
			
	def __len__(self): return self._len
	
	def Elements(self):
		if(self.isEmpty()): raise StopIteration("LL Empty")
		else:
			temp = self._head
			while(temp != None): 
				yield temp._value
				temp=temp._next
			
def Insert(LL1):
	LL1.Insert(Node(input("\n\tEnter a value = ")))

def Delete(LL1):
	if(LL1.isEmpty()): print("\n\tLL Empty")
	else: print("\n\tDeleted value = ", LL1.Delete())

def Display(LL1):
	print("\n\tLL : ", end='')
	for each in LL1.Elements():
		print(each, end=', ')
	print()

if __name__ == '__main__':
	LL1 = LL_Single()
	while 1:
		print("\n\t1. Insert\n\t2. Delete\n\t3. Display LL\n\t4. Length of LL\n\t5. Exit")
		try: ch = int(input("\tEnter your choice = "))
		except ValueError: ch=0
		
		if(ch==1): Insert(LL1)
		elif(ch==2): Delete(LL1)
		elif(ch==3): Display(LL1)
		elif(ch==4): print("\n\tLength = ", len(LL1))
		elif(ch==5): break
		else: print("\n\tInvalid Input ")
		input("\n\tPress Enter to continue...")
		
