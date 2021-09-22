from typing import Generic, TypeVar

T = TypeVar('T')



class LinkedQueue(Generic[T]):

    def __init__(self) -> None:
        self.clear()



    def is_empty(self) -> bool:
        return self.size == 0



    def is_initialized(self) -> None:
        return self.initialized



    def get_size(self) -> int:
        return self.size



    def enqueue(self, value) -> None:

        new = Node[T](value)

        if self.is_empty():
            self.head = new
            self.initialized = True

        else:
            self.tail.set_next(new)

        self.tail = new
        self.size += 1




    def get_front(self) -> T:

        if not self.is_initialized() or self.is_empty():
            raise Exception("Attempted to peek an empty queue!!!")

        result = self.head.get_value()
        return result




    def dequeue(self) -> T:

        if not self.is_initialized() or self.is_empty():
            raise Exception("Attempted to dequeue an empty queue!!!")

        temp = self.get_front()
        self.head = self.head.get_next()

        if self.head is None:
            self.tail = None

        self.size -= 1
        return temp




    def clear(self) -> None:
        self.initialized = False
        self.head = None
        self.tail = None
        self.size = 0




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