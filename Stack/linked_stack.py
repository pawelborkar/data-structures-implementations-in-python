from typing import TypeVar, Generic

T = TypeVar('T')

#############################
####### LINKED STACK ########

class LinkedStack(Generic[T]):

    def __init__(self) -> None:
        self.reset()




    # check if the stack is initialized
    def is_initialized(self) -> bool:
        return self.initialized




    # check if the stack is empty
    def is_empty(self) -> bool:
        return self.size == 0




    # add new node
    # time complexity: O(1)
    def push(self, item: T) -> None:

        self.size += 1
        self.initialized = True

        new = Node(item)
        new.set_next(self.head.get_next())
        self.head.set_next(new)




    # get the value in the front
    # time complexity: O(1)
    def peek(self) -> T:

        if not self.is_initialized() or self.is_empty():
            raise Exception("Attempted to peek an empty stack!!!")

        return self.head.get_next().get_value()




    # pop the value
    def pop(self) -> T:

        if not self.is_initialized() or self.is_empty():
            raise Exception("Attempted to pop an empty stack!!!")

        topValue = self.peek()
        self.head.set_next(self.head.get_next().get_next())
        self.size -= 1

        return topValue




    # get the size of the stack
    def get_size(self) -> int:
        return self.size




    # clear the stack
    def reset(self) -> None:
        self.initialized = False
        self.head = Node(None)
        self.size = 0




#######################
######### NODE ########
class Node(Generic[T]):

    def __init__(self, value: T) -> None:
        self.value = value
        self.next = None


    def get_value(self) -> T:
        return self.value


    def get_next(self) -> 'Node':
        return self.next


    def set_next(self, next) -> None:
        self.next = next