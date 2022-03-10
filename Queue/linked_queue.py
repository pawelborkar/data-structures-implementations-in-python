from queue import Empty
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class LinkedQueue(Generic[T]):

    def __init__(self) -> None:
        self._initialize()
        

    def enqueue(self, value) -> None:
        new_node = Node[T](value)

        if self.empty:
            self._head = new_node
            self._tail = new_node
            self._initialized = True
        else:
            self._tail.next = new_node

        self._tail = new_node
        self._size += 1


    def peek(self) -> T:
        if not self.initialized or self.empty:
            raise EmptyQueueException()

        result = self._head.value
        return result


    def dequeue(self) -> T:
        if not self.initialized or self.empty:
            raise EmptyQueueException()

        item = self.peek()
        self._head = self._head.next

        if self._head is None:
            self._tail = None

        self._size -= 1
        return item
    

    def clear(self) -> None:
        self._initialize()
        
    
    def _initialize(self) -> None:
        self._initialized = False
        self._head = None
        self._tail = None
        self._size = 0
        
    
    @property
    def initialized(self) -> None:
        return self._initialized
    
    
    @property
    def empty(self) -> bool:
        return self._size == 0
    
    
    def __bool__(self) -> bool:
        return self._size != 0
    
    
    def __len__(self) -> int:
        return self._size
    
    
    def __iter__(self):
        self._current = self._head
        return self
    
    
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            item = self._current.value
            self._current = self._current.next
            return item



class Node(Generic[T]):

    def __init__(self, value: T):
        self._value: T = value
        self._next: Optional[Node] = None

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next
    
    @value.setter
    def value(self, value):
        self.value = value

    @next.setter
    def next(self, next):
        self._next = next
        
        
        
class EmptyQueueException(Exception):
    def __init__(self) -> None:
        super().__init__("Attempted to retrieve value from an empty queue")