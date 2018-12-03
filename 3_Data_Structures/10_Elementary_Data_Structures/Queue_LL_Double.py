class Node:

    def __init__(self, Value=None, Prev=None, Next=None):
        self.value = Value
        self.next = Next
        self.prev = Prev

class Queue_LLD:

    def __init__(self):
        self.__head = Node()
        self.__tail = Node(Prev = self.__head)
        self.__head.next = self.__tail
        self.__len = 0
        self.__i = None

    def is_empty(self):
        return self.__len == 0

    def enqueue(self, Value):
        temp = Node(Value, self.__tail.prev, self.__tail)
        self.__tail.prev.next  = temp
        self.__tail.prev = temp
        self.__len += 1

    def dequeue(self):
        if(self.is_empty()): raise IndexError("Queue is Empty")
        else:
            temp = self.__head.next
            self.__head.next = temp.next
            temp.next.prev = self.__head
            self.__len -= 1
            return temp.value

    def __len__(self):
        return self.__len

    def __next__(self):
        if( self.__i != self.__tail ):
            self.__i = self.__i.next
            return self.__i.prev.value
        else: raise StopIteration()

    def __iter__(self):
        self.__i = self.__head.next
        return self

    def __str__(self):
        Values = []
        for i in self:
            Values.append(str(i))

        return ", ".join(Values)

if __name__ == '__main__':

    Q_LL1 = Queue_LLD()

    for i in range(5):
        print("Insert", i)
        Q_LL1.enqueue(i)

    print("\nQueue :", end="")
    for i in Q_LL1:
        print(i, end=", ")

    print("\n\nDequeue, Deleted value = ", Q_LL1.dequeue())

    print("\nDequeue = ", Q_LL1)
