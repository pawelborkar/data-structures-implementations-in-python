class Stack:

    def __init__(self) -> None:
        self.arr = []
        


    def push(self, val):
        self.arr.append(val)
        


    def pop(self):

        if self.get_size() == 0:
            raise Exception('empty stack')

        return self.arr.pop()
    


    def peek(self):
        return self.arr[self.get_size() - 1]
    


    def get_size(self):
        return len(self.arr)
    
    

    def clear(self):
        self.arr = []

        


class QueueFromStack:

    def __init__(self) -> None:
        self.in_stack = Stack()
        self.out_stack = Stack()
        


    def enqueue(self, val):
        self.in_stack.push(val)
        


    def dequeue(self):

        if self.out_stack.get_size() == 0:

            for _ in range(self.in_stack.get_size()):

                self.out_stack.push(self.in_stack.pop())

        return self.out_stack.pop()
    


    def get_front(self):

        if self.out_stack.get_size() == 0:

            for _ in range(self.in_stack.get_size()):

                self.out_stack.push(self.in_stack.pop())

        return self.out_stack.peek()
    


    def get_size(self):
        return self.in_stack.get_size() + self.out_stack.get_size()



    def clear(self):
        self.in_stack.clear()
        self.out_stack.clear()
    