############################
####### ARRAY STACK ########
class ArrayStack:
    def __init__(self) -> None:
        self.reset()

    # add new item on top of the stack
    # time complexity: O(1)
    def push(self, value):
        self.initialized = True
        self.arr.append(value)

    # remove and return the item at the top of the stack
    # time complexity: O(1)
    def pop(self):
        if self.is_empty():
            raise Exception('Attempted to pop an empty stack!!!')
        return self.arr.pop()

    # get the item at the top of the stack
    # time complexity: O(1)
    def peek(self):
        if self.is_empty():
            raise Exception('Attempted to peek an empty stack!!!')
        return self.arr[self.get_size() - 1]

    # return the size of the stack
    def get_size(self):
        return len(self.arr)

    # check if the stack is empty
    def is_empty(self):
        return self.get_size() == 0

    # empty the stack
    def reset(self):
        self.arr = []
        self.initialized = False



#############################
####### LINKED STACK ########
class LinkedStack:
    def __init__(self) -> None:
        self.reset()

    # check if the stack is initialized
    def is_initialized(self):
        return self.initialized

    # check if the stack is empty
    def is_empty(self):
        return self.size == 0

    # add new node
    # time complexity: O(1)
    def push(self, item):
        self.size += 1
        self.initialized = True
        new = Node(item)
        new.set_next(self.head.get_next())
        self.head.set_next(new)

    # get the value in the front
    # time complexity: O(1)
    def peek(self):
        if not self.is_initialized() or self.is_empty():
            raise Exception("Attempted to peek an empty stack!!!")
        return self.head.get_next().get_value()

    # pop the value
    def pop(self):
        if not self.is_initialized() or self.is_empty():
            raise Exception("Attempted to pop an empty stack!!!")
        topValue = self.peek()
        self.head.set_next(self.head.get_next().get_next())
        self.size -= 1
        return topValue

    # get the size of the stack
    def get_size(self):
        return self.size

    # clear the stack
    def reset(self):
        self.initialized = False
        self.head = Node(None)
        self.size = 0



#######################
######### NODE ########
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next