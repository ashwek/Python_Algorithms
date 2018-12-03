class Stack:

    def __init__(self, Size=10):
        self.__size = Size
        self.__stack = []
        self.__i = -1

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__size

    def push(self, value):
        if(self.is_full()): raise IndexError("Overflow Error - Stack is Full")
        else: self.__stack.append(value)

    def pop(self):
        if(self.is_empty()): raise IndexError("Unerflow Error - Stack is Empty")
        return self.__stack.pop()

    def top(self):
        if(self.is_empty()): raise IndexError("Stack is Empty")
        return self.__stack[-1]

    def __len__(self):
        return len(self.__stack)

    def __getitem__(self, index):
        if(index < len(self)): return self.__stack[index]
        else: raise IndexError()

    def __next__(self):
        self.__i += 1
        if(self.__i < len(self)): return self.__stack[self.__i]
        else: raise StopIteration()

    def __iter__(self):
        self.__i = -1
        return self

    def __str__(self):
        Values = []
        for i in self.__stack:
            Values.append(str(i))

        return ", ".join(Values)

if __name__ == '__main__':

    S1 = Stack(5)

    for i in range(5):
        print("Insert", i, "in stack")
        S1.push(i)

    print("\nStack : ", end="")
    for i in S1:
        print(i, end=", ")

    print("\n\nPop, popped element = ", S1.pop())

    print("\nStack :", S1)
