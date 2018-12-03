class Queue_Circular:

    def __init__(self, Size=10):
        self.__size = Size+1
        self.__queue = [None]*(Size+1)
        self.__head = self.__tail = 0
        self.__i = -1

    def is_empty(self):
        return self.__head == self.__tail

    def is_full(self):
        return (self.__tail+1)%self.__size == self.__head

    def enqueue(self, value):
        if(self.is_full()): raise IndexError("Overflow Error - Queue is Full")
        self.__queue[self.__tail] = value
        self.__tail = (self.__tail+1)%self.__size

    def dequeue(self):
        if(self.is_empty()): raise IndexError("Unerflow Error - Queue is Empty")
        self.__head = (self.__head+1)%self.__size
        return self.__queue[(self.__head-1)%self.__size]

    def head(self):
        if(self.is_empty()): raise IndexError("Queue is Empty")
        return self.__queue[self.__head]

    def tail(self):
        if(self.is_empty()): raise IndexError("Queue is Empty")
        return self.__queue[(self.__tail-1)%self.__size]

    def __len__(self):
        return self.__tail-self.__head if(self.__tail>=self.__head) else self.__size-self.__head+self.__tail

    def __getitem__(self, index):
        if(0 <= index < len(self)):
            return self.__queue[(index+self.__head)%self.__size]
        else: raise IndexError("Index out of range")

    def __next__(self):
        self.__i += 1
        if(self.__i < len(self)): return self.__getitem__(self.__i)
        else: raise StopIteration()

    def __iter__(self):
        self.__i = -1
        return self

    def __str__(self):
        Values = []
        for i in self:
            Values.append(str(i))

        return ", ".join(Values)


if __name__ == '__main__':

    Q1 = Queue_Circular(5)

    for i in range(5):
        print("Insert / enqueue", i)
        Q1.enqueue(i)

    print("\nQueue : ", end="")
    for i in Q1:
        print(i, end=", ")

    print("\n\nDelete / dequeue, deleted value = ", Q1.dequeue())

    print("\nQueue :", Q1)
