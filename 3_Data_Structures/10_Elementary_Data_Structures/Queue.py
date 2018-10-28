class Queue:
	
	def __init__(self, Size=10):
		self._size = Size
		self._queue=[None]*Size
		self._head = self._tail = 0
		self._i=-1
	
	def isEmpty(self): return self._head == self._tail
	def isFull(self): return self._tail == self._size
	
	def EnQueue(self, value):
		if(self.isFull()): raise IndexError("Overflow Error - Queue is Full")
		self._queue[self._tail]=value
		self._tail+=1
		
	def DeQueue(self):
		if(self.isEmpty()): raise IndexError("Unerflow Error - Queue is Empty")
		self._head+=1
		return self._queue[self._head-1]
		
	def Head(self):
		if(self.isEmpty()): raise IndexError("Queue is Empty")
		return self._queue[self._head]
	
	def Tail(self):
		if(self.isEmpty()): raise IndexError("Queue is Empty")
		return self._queue[self._tail-1]
	
	def __len__(self):return self._tail-self._head
		
	def __getitem__(self, index):
		if(self._head <= (index+self._head) < self._tail):
			return self._queue[index+self._head]
		else: raise IndexError("Index out of range")
		
	def __next__(self):
		self._i+=1 
		if(self._i < self.__len__()): return self.__getitem__(self._i)
		else: raise StopIteration()
		
	def __iter__(self):
		self._i=-1
		return self
		
def Enqueue(Q1):
	if(Q1.isFull()): print("\n\tOverflow Error - Queue is Full")
	else: Q1.EnQueue(input("\n\tEnter value to enqueue in Queue = "))
	
def Dequeue(Q1):
	try: print("\n\tDequeued Value = ", Q1.DeQueue())
	except IndexError: print("\n\tUnerflow Error - Queue is Empty")
	
def See_Head_Tail(Q1):
	try: print("\n\tHead Value = ", Q1.Head(), "\tTail Value = ", Q1.Tail())
	except IndexError: print("\n\tQueue is Empty")
	
def Display(Q1):
	print("\n\tQueue : ", end='')
	for each in Q1: print(each, end=', ')
		
if __name__ == '__main__':
	try: Size = int(input("\n\tEnter size of queue = "))
	except ValueError: Size=5
	
	Q1 = Queue(Size)
	while 1:
		print("\n\t1. Enqueue\n\t2. Dequeue\n\t3. See Head and Tail\n\t4. Display Queue\n\t5. Length of Queue\n\t6. Exit")
		try: ch = int(input("\tEnter your choice = "))
		except ValueError: ch=0
		
		if(ch==1): Enqueue(Q1)
		elif(ch==2): Dequeue(Q1)
		elif(ch==3): See_Head_Tail(Q1)
		elif(ch==4): Display(Q1)
		elif(ch==5): print("\n\tLength = ", len(Q1))
		elif(ch==6): break
		else: print("\n\tInvalid Input ")
		input("\n\tPress Enter to continue...")
		
