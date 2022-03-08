from queue import Empty
from typing import Generic, TypeVar

T = TypeVar('T')


class LinkedQueue(Generic[T]):

    def __init__(self) -> None:
        self._initialize()
        

    def enqueue(self, value) -> None:
        new_node = Node[T](value)

        if self.is_empty:
            self._head = new_node
            self._initialized = True
        else:
            self.tail.set_next(new_node)

        self.tail = new_node
        self._size += 1


    def get_front(self) -> T:
        if not self.is_initialized or self.is_empty:
            raise EmptyQueueException()

        result = self._head.value()
        return result


    def dequeue(self) -> T:
        if not self.is_initialized or self.is_empty:
            raise EmptyQueueException()

        temp = self.get_front()
        self._head = self._head.get_next()

        if self._head is None:
            self.tail = None

        self._size -= 1
        return temp
    

    def clear(self) -> None:
        self._initialize()
        
    
    def _initialize(self) -> None:
        self._initialized = False
        self._head = None
        self.tail = None
        self._size = 0
        
    
    @property
    def is_initialized(self) -> None:
        return self._initialized
    
    
    @property
    def is_empty(self) -> bool:
        return self._size == 0
    
    
    def __bool__(self) -> bool:
        return self._size != 0
    
    
    def __len__(self) -> int:
        return self._size




class Node(Generic[T]):

    def __init__(self, value: T) -> None:
        self._value: T = value
        self._next: Optional[Node] = None

    def value(self) -> T:
        return self._value

    def get_next(self) -> Optional[Node]:
        return self._next

    def set_next(self, next) -> None:
        self._next = next
        
        
        
class EmptyQueueException(Exception):
    def __init__(self) -> None:
        super.__init__("Attempted to retrieve value from an empty queue")