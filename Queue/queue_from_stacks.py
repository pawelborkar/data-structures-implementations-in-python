from typing import Any

class Stack:

    def __init__(self) -> None:
        self.arr = list()

    def push(self, val) -> None:
        self.arr.append(val)

    def pop(self) -> Any:
        if self.size == 0:
            raise Exception('empty stack')
        return self.arr.pop()

    def peek(self) -> Any:
        return self.arr[-1]
    
    def clear(self) -> None:
        self.arr = list()
        
    @property
    def size(self) -> int:
        return len(self.arr)

        
class QueueFromStack:

    def __init__(self) -> None:
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, val) -> None:
        self.in_stack.push(val)
        
    def dequeue(self) -> Any:
        if self.size == 0:
            raise Exception("Empty Queue")
        if self.out_stack.size == 0:
            for _ in range(self.in_stack.size):
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()
    
    def peek(self) -> Any:
        if self.size == 0:
            raise Exception("Empty Queue")
        if self.out_stack.size == 0:
            for _ in range(self.in_stack.size):
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()

    def clear(self) -> None:
        self.in_stack.clear()
        self.out_stack.clear()

    @property
    def size(self) -> int:
        return self.in_stack.size + self.out_stack.size
    
    def __len__(self) -> int:
        return self.size
    
    def __bool__(self) -> int:
        return self.size != 0
