import sys


class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 1
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize
        self.minvals = [sys.maxsize] * (stacksize * self.numstacks)

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception("Stack is full")
        self.sizes[stacknum] += 1
        if self.IsEmpty(stacknum):
            self.minvals[self.IndexOfTop(stacknum)] = item
        else:
            self.minvals[self.IndexOfTop(stacknum)] = min(
                item, self.minvals[self.IndexOfTop(stacknum) - 1]
            )
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception("Stack is empty")
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception("Stack is empty")
        return self.array[self.IndexOfTop(stacknum)]

    def Min(self, stacknum):
        return self.minvals[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1


# Optimized Solution for this problem
class StackNode(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class StackMin(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * self.capacity
        self._min = []
    
    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size == 0
    
    def push(self, value):
        if self.isFull():
            raise Exception('Stack is Full')
        if self.isEmpty():
            self._min.append(value)
            self.array[self.size] = value
            self.size += 1
        else:
            if value <= self._min[-1]:
                self._min.append(value)
            self.size += 1
            self.array[self.size-1] = value
        return True
        
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        popped = self.array[self.size-1]
        if self._min[-1] == popped.value:
            _ = self._min.pop()
        self.array[idx] = 0
        self.size -= 1
        return popped.value
    
    def min(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        return self._min[-1]


def multistacksolution():
    newstack = MultiStack(10)
    newstack.Push(5, 0)
    newstack.Push(6, 0)
    newstack.Push(2, 0)
    newstack.Push(7, 0)
    newstack.Push(14, 0)
    newstack.Push(3, 0)
    print(newstack.Min(0))
    newstack.Push(1, 0)
    newstack.Push(4, 0)
    newstack.Push(44, 0)
    newstack.Push(2, 0)
    print(newstack.Min(0))

def stackminsolution():
    newstack = StackMin(10)
    newstack.push(5)
    newstack.push(6)
    newstack.push(2)
    newstack.push(7)
    newstack.push(14)
    newstack.push(3)
    print(newstack.min())
    newstack.push(1)
    newstack.push(4)
    newstack.push(44)
    newstack.push(2)
    print(newstack.min())

if __name__ == "__main__":
    multistacksolution()
    print('*'*5)
    stackminsolution()
