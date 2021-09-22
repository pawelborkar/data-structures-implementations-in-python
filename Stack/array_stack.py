from typing import TypeVar, Generic

T = TypeVar('T')


############################
####### ARRAY STACK ########

class ArrayStack(Generic[T]):

    def __init__(self) -> None:
        self.reset()




    # add new item on top of the stack
    # time complexity: O(1)
    def push(self, value: T) -> None:
        self.initialized = True
        self.arr.append(value)




    # remove and return the item at the top of the stack
    # time complexity: O(1)
    def pop(self) -> T:

        if self.is_empty():
            raise Exception('Attempted to pop an empty stack!!!')

        return self.arr.pop()




    # get the item at the top of the stack
    # time complexity: O(1)
    def peek(self) -> T:

        if self.is_empty():
            raise Exception('Attempted to peek an empty stack!!!')

        return self.arr[self.get_size() - 1]




    # return the size of the stack
    def get_size(self) -> int:
        return len(self.arr)




    # check if the stack is empty
    def is_empty(self) -> bool:
        return self.get_size() == 0




    # empty the stack
    def reset(self) -> None:
        self.arr = []
        self.initialized = False