class Node:
	def __init__(self, Value=None, Prev=None, Next=None):
		self.__value = Value
		self.__next = Next
		self.__prev = Prev

	def get_value(self): return self.__value
	def set_next(self, Next): self.__next=Next
	def get_next(self): return self.__next
	def set_prev(self, Prev): self.__prev=Prev
	def get_prev(self): return self.__prev
			
class LL_Double:
	def __init__(self):
		self._head = Node()
		self._tail = Node(Prev=self._head)
		self._head.set_next(self._tail)
		self._len = 0
		
	def isEmpty(self): return self._len==0
	
	def EnQueue(self, Value):
		temp = Node(Value, self._tail.get_prev(), self._tail)
		self._tail.get_prev().set_next(temp)
		self._tail.set_prev(temp)
		self._len+=1
	
	def DeQueue(self):
		if(self.isEmpty()): raise IndexError("Queue is Empty")
		else:
			temp = self._head.get_next()
			self._head.set_next(temp.get_next())
			temp.get_next().set_prev(self._head)
			self._len-=1
			return temp.get_value()
			
	def __len__(self): return self._len
	
	def Elements(self):
		if(self.isEmpty()): raise StopIteration("Queue is Empty")
		else:
			temp = self._head.get_next()
			while(temp != self._tail): 
				yield temp.get_value()
				temp=temp.get_next()
		
def EnQueue(Q_LL1): Q_LL1.EnQueue(input("\n\tEnter a value = "))

def DeQueue(Q_LL1):
	if(Q_LL1.isEmpty()): print("\n\tQueue is Empty")
	else: print("\n\tDeleted value = ", Q_LL1.DeQueue())

def Display(Q_LL1):
	print("\n\tQueue : (", end='')
	for each in Q_LL1.Elements(): print(each, end=', ')
	print(')')

if __name__ == '__main__':
	Q_LL1 = LL_Double()
	while 1:
		print("\n\t1. EnQueue\n\t2. DeQueue\n\t3. Display Queue\n\t4. Length of Queue\n\t5. Exit")
		try: ch = int(input("\tEnter your choice = "))
		except ValueError: ch=0
		
		if(ch==1): EnQueue(Q_LL1)
		elif(ch==2): DeQueue(Q_LL1)
		elif(ch==3): Display(Q_LL1)
		elif(ch==4): print("\n\tLength = ", len(Q_LL1))
		elif(ch==5): break
		else: print("\n\tInvalid Input ")
		input("\n\tPress Enter to continue...")
